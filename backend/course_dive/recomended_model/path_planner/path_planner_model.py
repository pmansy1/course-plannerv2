import networkx as nx
import pandas as pd
import re
import random
from collections import defaultdict

class UserStudent:
    def __init__(self, user_id, name, age, major, minor, year, exp_grad_year, credits_completed, completed_courses, interests=None):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.major = major
        self.minor = minor
        self.year = year
        self.exp_grad_year = exp_grad_year
        self.credits_completed = credits_completed
        self.completed_courses = [self._normalize(c) for c in completed_courses]
        self.courses_rec = []
        self.interests = []
        self.add_interest(interests or [])

    def _normalize(self, course):
        return course.strip().lower().replace('.', '').replace('-', '').replace(' ', '')

    def add_interest(self, interest_list):
        for interest in interest_list:
            if interest not in self.interests:
                self.interests.append(interest)

    def remove_interest(self, interest):
        if interest in self.interests:
            self.interests.remove(interest)

    def update_courses(self, courses):
        for course in courses:
            norm_course = self._normalize(course)
            if norm_course not in self.courses_rec:
                self.courses_rec.append(norm_course)

    def get_user_profile(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "age": self.age,
            "major": self.major,
            "minor": self.minor,
            "year": self.year,
            "exp_grad_year": self.exp_grad_year,
            "credits_completed": self.credits_completed,
            "completed_courses": self.completed_courses,
            "courses_rec": self.courses_rec,
            "interests": self.interests
        }

    def __str__(self):
        return (
            f"User ID: {self.user_id}, Name: {self.name}, Major: {self.major}, "
            f"Year: {self.year}, Completed Courses: {self.completed_courses}"
        )
    

class PathPlanner:
    MAX_CREDITS_PER_QUARTER = 18
    MAX_COURSES_PER_QUARTER = 6
    QUARTERS = ["Fall", "Winter", "Spring"]

    def __init__(self, recommender_df: pd.DataFrame):
        # Load your full course catalog (pamphlet) with detailed course info
        self.pamphlet_df = pd.read_csv('/Users/joy/Downloads/preprocessed_courses_high_quality_keywords.csv')

        # Add normalized course code column by extracting from course titles
        self.pamphlet_df["Normalized Code"] = self.pamphlet_df["Course Title"].apply(self.extract_course_code)

        # Recommender dataframe (course codes, prereqs, etc)
        self.recommender_df = recommender_df.copy()
        self.recommender_df["Normalized Code"] = self.recommender_df["Course Code"].apply(self.normalize_code)

        # Fix any missing or incorrect column names (example: credit_hours)
        if "credit_houurs" in self.pamphlet_df.columns:
            self.pamphlet_df.rename(columns={"credit_houurs": "credit_hours"}, inplace=True)

        # Build prerequisite graph from recommender_df
        self.graph = nx.DiGraph()
        self.build_graph()

    @staticmethod
    def normalize_code(code):
        if not isinstance(code, str):
            return ""
        return code.strip().lower().replace('.', '').replace('-', '').replace(' ', '')

    @staticmethod
    def extract_course_code(title):
        if not isinstance(title, str):
            return None
        # Extract e.g. "CA 2100" or "MKTG 3460"
        match = re.search(r"\b([A-Z]{2,})\s*(\d{3,4})\b", title)
        if match:
            return (match.group(1) + match.group(2)).lower()
        return None

    def build_graph(self):
        self.graph.clear()
        for _, row in self.recommender_df.iterrows():
            course_code = self.normalize_code(row.get("Course Code", ""))
            self.graph.add_node(course_code)

            prereq_str = str(row.get("Prerequisites", "") or "")
            # Extract all course codes in prereq string
            prereq_matches = re.findall(r"\b([A-Z]{2,})\s*(\d{3,4})\b", prereq_str)
            for dept, num in prereq_matches:
                prereq_code = self.normalize_code(f"{dept} {num}")
                if prereq_code:
                    self.graph.add_edge(prereq_code, course_code)

    def get_course_title(self, normalized_code):
        row = self.pamphlet_df[self.pamphlet_df["Normalized Code"] == normalized_code]
        if not row.empty:
            return row.iloc[0]["Course Title"]
        else:
            # fallback to upper code
            return normalized_code.upper()

    def get_course_credits(self, normalized_code):
        row = self.pamphlet_df[self.pamphlet_df["Normalized Code"] == normalized_code]
        if row.empty:
            return 4  # default fallback
        credits = row.iloc[0].get("credit_hours", 4)
        if isinstance(credits, (int, float)):
            return int(credits)
        return 4

    def get_ordered_prereq_chain(self, target_code):
        """
        Returns the list of prerequisites in order from first to last for the target course.
        If no prereqs, returns empty list.
        """
        if target_code not in self.graph:
            return []

        # Use topological sort of the subgraph of all ancestors + target
        ancestors = nx.ancestors(self.graph, target_code)
        subgraph_nodes = ancestors.union({target_code})
        subgraph = self.graph.subgraph(subgraph_nodes)

        ordered_courses = list(nx.topological_sort(subgraph))
        # Remove the target from the beginning if it appears first, ensure it's at the end
        if ordered_courses[-1] != target_code:
            ordered_courses.remove(target_code)
            ordered_courses.append(target_code)
        return ordered_courses

    def filter_no_prereq_courses(self):
        # Returns dataframe of courses with empty or null prereqs
        return self.recommender_df[self.recommender_df["Prerequisites"].isnull() | 
                                   (self.recommender_df["Prerequisites"].str.strip() == "")]

    def fill_with_basics(self, courses_taken_norm, credits_needed):
        """
        Fill credits_needed by randomly selecting from no-prereq courses not yet taken.
        Returns list of tuples (normalized_code, credits)
        """
        basics = []
        no_prereq_df = self.filter_no_prereq_courses()
        # Exclude already taken courses
        eligible = no_prereq_df[~no_prereq_df["Normalized Code"].isin(courses_taken_norm)]
        eligible = eligible.sample(frac=1).reset_index(drop=True)  # shuffle

        for _, row in eligible.iterrows():
            if credits_needed <= 0:
                break
            code = self.normalize_code(row["Course Code"])
            credits = int(row.get("Credits", 4))
            basics.append((code, credits))
            credits_needed -= credits
        return basics

    def plan_path(self, completed_courses, target_course_code, interests=None, major=None):
        """
        Plan a 3-quarter schedule to reach target_course_code starting from completed_courses.
        Fill leftover credits with basics.
        Returns dict of quarter -> list of tuples (full_course_title, credits)
        """
        completed_norm = set(self.normalize_code(c) for c in completed_courses)
        target_norm = self.normalize_code(target_course_code)

        planned = defaultdict(list)
        credits_used = {q: 0 for q in self.QUARTERS}
        courses_planned = set(completed_norm)

        # If target already completed, just fill all quarters with basics
        if target_norm in courses_planned:
            for q in self.QUARTERS:
                remaining_credits = self.MAX_CREDITS_PER_QUARTER
                basics = self.fill_with_basics(courses_planned, remaining_credits)
                for code, cr in basics:
                    planned[q].append((self.get_course_title(code), cr))
                    courses_planned.add(code)
            return planned

        # Get ordered prerequisite chain (including target)
        prereq_chain = self.get_ordered_prereq_chain(target_norm)

        quarter_index = 0

        for course_code in prereq_chain:
            if course_code in courses_planned:
                continue
            credits = self.get_course_credits(course_code)

            # Schedule course respecting credit and course limits
            placed = False
            while not placed and quarter_index < len(self.QUARTERS):
                q = self.QUARTERS[quarter_index]
                if (credits_used[q] + credits <= self.MAX_CREDITS_PER_QUARTER and
                    len(planned[q]) < self.MAX_COURSES_PER_QUARTER):
                    planned[q].append((self.get_course_title(course_code), credits))
                    credits_used[q] += credits
                    courses_planned.add(course_code)
                    placed = True
                else:
                    quarter_index += 1
            if not placed:
                # If cannot place due to credit/course limits, break early
                break

        # Fill remaining quarters with basics if credits left
        for q in self.QUARTERS:
            remaining_credits = self.MAX_CREDITS_PER_QUARTER - credits_used[q]
            if remaining_credits > 0:
                basics = self.fill_with_basics(courses_planned, remaining_credits)
                for code, cr in basics:
                    planned[q].append((self.get_course_title(code), cr))
                    courses_planned.add(code)

        return planned
