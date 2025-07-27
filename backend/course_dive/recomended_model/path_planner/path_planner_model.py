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
    MIN_COURSES_PER_QUARTER = 2
    QUARTERS = ["Fall", "Winter", "Spring"]

    def __init__(self, recommender_df: pd.DataFrame):
        self.pamphlet_df = pd.read_csv(
            "/Users/joy/Downloads/preprocessed_courses_high_quality_keywords.csv"
        )
        self.recommender_df = recommender_df.copy()

        # Normalize codes for pamphlet_df
        self.pamphlet_df["Normalized Code"] = self.pamphlet_df["Course Title"].apply(
            self.extract_course_code
        )
        # Normalize prerequisites column
        if "prerequisites" in self.pamphlet_df.columns:
            self.pamphlet_df["Normalized Prereqs"] = self.pamphlet_df["prerequisites"].apply(
                self.normalize_prereq_string
            )
        else:
            self.pamphlet_df["Normalized Prereqs"] = [[]]

        self.recommender_df["Normalized Code"] = self.recommender_df["Course Code"].apply(
            self._normalize_code
        )


        self.graph = nx.DiGraph()
        self.build_graph()

    def _normalize_code(self, code):
        if not isinstance(code, str):
            return ""
        return code.strip().lower().replace(".", "").replace("-", "").replace(" ", "")

    def extract_course_code(self, text):
        if not isinstance(text, str):
            return None
        match = re.search(r"\b([A-Za-z]{2,5})\s*(\d{3,4})\b", text)
        if match:
            return (match.group(1) + match.group(2)).lower()
        return None

    def normalize_prereq_string(self, prereq_str):
        if not isinstance(prereq_str, str) or prereq_str.strip() == "":
            return []
        matches = re.findall(r"\b([A-Za-z]{2,5})\s*0*(\d{3,4})\b", prereq_str)
        return [self._normalize_code(f"{dept} {num}") for dept, num in matches]

    def build_graph(self):
        self.graph.clear()
        for _, row in self.pamphlet_df.iterrows():
            course_code = row.get("Normalized Code")
            if not course_code:
                continue
            self.graph.add_node(course_code)
            prereqs = row.get("Normalized Prereqs", [])
            for prereq in prereqs:
                self.graph.add_edge(prereq, course_code)

    def get_course_title(self, normalized_code):
        row = self.pamphlet_df[self.pamphlet_df["Normalized Code"] == normalized_code]
        if not row.empty:
            return row.iloc[0]["Course Title"]
        return f"{normalized_code.upper()} (Unknown Title)"

    def get_course_credits(self, normalized_code):
        row = self.pamphlet_df[self.pamphlet_df["Normalized Code"] == normalized_code]
        if row.empty:
            return 4
        credits = row.iloc[0].get("credit_hours", 4)
        try:
            return int(float(credits))
        except:
            return 4

    def get_prerequisites_for_course(self, normalized_code):
        row = self.pamphlet_df[self.pamphlet_df["Normalized Code"] == normalized_code]
        if row.empty:
            print(f"[DEBUG] No pamphlet entry for course: {normalized_code}")
            return []
        print(f"[DEBUG] Prereqs for {normalized_code}: {row.iloc[0].get('Normalized Prereqs', [])}")
        return row.iloc[0].get("Normalized Prereqs", [])

    def expand_prerequisite_chain(self, target_norm):
        """Recursively expand prerequisites including nested ones."""
        chain = []
        stack = [target_norm]
        seen = set()

        print(f"[DEBUG] Expanding prereq chain for target: {target_norm}")
        while stack:
            course = stack.pop()
            if course in seen:
                continue
            seen.add(course)
            prereqs = self.get_prerequisites_for_course(course)
            for pre in prereqs:
                if pre not in seen:
                    stack.append(pre)
                    chain.append(pre)

        chain.reverse()
        print(f"[DEBUG] Final prereq chain for {target_norm}: {chain}")
        return chain

    def filter_no_prereq_courses(self):
        return self.pamphlet_df[
            self.pamphlet_df["Normalized Prereqs"].apply(lambda x: len(x) == 0)
        ]

    def fill_with_basics(self, courses_taken, needed_count, allow_zero_credit=True):
        basics = []
        no_prereq_df = self.filter_no_prereq_courses()
        eligible = no_prereq_df[
            ~no_prereq_df["Normalized Code"].isin(courses_taken)
        ].sample(frac=1)

        zero_credit_used = False
        for _, row in eligible.iterrows():
            if len(basics) >= needed_count:
                break
            norm_code = row["Normalized Code"]
            credits = self.get_course_credits(norm_code)
            if credits == 0:
                if zero_credit_used or not allow_zero_credit:
                    continue
                zero_credit_used = True
            basics.append((row["Course Title"], credits))
        return basics

    def plan_path(self, completed_courses, target_course_code, interests, major):
        completed_norm = set(self._normalize_code(c) for c in completed_courses)
        target_norm = self._normalize_code(target_course_code)
        print(f"[DEBUG] Target normalized: {target_norm}")
        print(f"[DEBUG] Completed normalized: {completed_norm}")
        # Expand prerequisite chain
        prereq_chain = self.expand_prerequisite_chain(target_norm)
        full_chain = prereq_chain + [target_norm]
        print(f"[DEBUG] Full chain: {full_chain}")
        planned = defaultdict(list)
        credits_used = {q: 0 for q in self.QUARTERS}
        courses_planned = set(completed_norm)
        quarter_index = 0

        # Place prereqs and target
        for course in full_chain:
            if course in courses_planned:
                print(f"[DEBUG] Skipping {course}, already completed.")
                continue
            credits = self.get_course_credits(course)
            print(f"[DEBUG] Trying to place {course} ({credits} credits)")
            placed = False
            while quarter_index < len(self.QUARTERS):
                q = self.QUARTERS[quarter_index]
                if (
                    len(planned[q]) < self.MAX_COURSES_PER_QUARTER
                    and credits_used[q] + credits <= self.MAX_CREDITS_PER_QUARTER
                ):
                    planned[q].append((self.get_course_title(course), credits))
                    credits_used[q] += credits
                    courses_planned.add(course)
                    placed = True
                    print(f"[DEBUG] Placed {course} in {q}")
                    break
                else:
                    quarter_index += 1
            if not placed:
                print(f"[DEBUG] Could NOT place {course} (ran out of quarters).")
                # Not enough quarters → stop early (future: extend beyond 3 quarters)
                break

        # Fill each quarter to meet min/max rules
        for q in self.QUARTERS:
            current_count = len(planned[q])
            if current_count < self.MIN_COURSES_PER_QUARTER:
                needed = self.MIN_COURSES_PER_QUARTER - current_count
                basics = self.fill_with_basics(courses_planned, needed)
                planned[q].extend(basics)

            while len(planned[q]) < self.MAX_COURSES_PER_QUARTER:
                basics = self.fill_with_basics(courses_taken=courses_planned, needed_count=1)
                if not basics:
                    break
                planned[q].extend(basics)

        return planned
    