import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import pandas as pd
import re

class CourseRecommender:
    def __init__(self, course_df):
        self.course_df = course_df.copy()
        self.vectorizer = TfidfVectorizer()
        self.course_vectors = None
        self.pamphlet_df = pd.read_csv('/Users/joy/Downloads/preprocessed_courses_high_quality_keywords.csv')  # Placeholder for pamphlet DataFrame
        self.pamphlet_df["Course Code"] = self.pamphlet_df["Course Title"].apply(self.extract_course_code)
    def extract_course_code(self, title):
        match = re.search(r"\b([A-Za-z]{2,})\s*0*?(\d{3,4})\b", title)
        if match:
            return (match.group(1) + match.group(2)).upper()
        return None
    
    def fit(self):
        if "Keywords" not in self.course_df.columns:
            raise ValueError("Missing 'Keywords' in course DataFrame.")
        self.course_vectors = self.vectorizer.fit_transform(self.course_df["Keywords"].fillna(""))

    def recommend(self, user_profile, top_n=10):
        if self.course_vectors is None:
            raise ValueError("Model not trained. Call fit() first.")

        interests = user_profile.get("interests", [])
        interests_text = " ".join(interests)
        interest_vector = self.vectorizer.transform([interests_text])
        cosine_scores = cosine_similarity(interest_vector, self.course_vectors).flatten()
        
        major = user_profile.get("major", "").lower()
        difficulty_pref = user_profile.get("difficulty_preference", "").lower()
        recommendations = []

        for idx, row in self.course_df.iterrows():
            base_score = cosine_scores[idx]
            course_keywords = row.get("Keywords", "").lower().split()
            course_difficulty = row.get("Difficulty", "").lower()
            major_bonus = 0.0
            department = self.pamphlet_df['Course']
            # --- Interest bonus: exponential boost ---
            interest_matches = sum(1 for kw in interests if kw.lower() in course_keywords)
            interest_bonus = 0.18 * (interest_matches ** 1.5) if interest_matches > 0 else 0
            
            raw_title = row.get("Course Title", "")
            extracted_code = self.extract_course_code(raw_title)

            # --- Find department from pamphlet ---
            pamphlet_match = self.pamphlet_df[
                self.pamphlet_df["Course Code"] == extracted_code
            ]

            department = "UNKNOWN"
            credits = row.get("Credits", 4)  # fallback

            if not pamphlet_match.empty:
                department = pamphlet_match.iloc[0]["Course"]
                credits = (
                    pamphlet_match.iloc[0]["credit_hours"]
                    if "credit_hours" in pamphlet_match.columns
                    else credits
                )


            # --- Difficulty bonus (optional) ---
            difficulty_bonus = 0.05 if difficulty_pref and difficulty_pref in course_difficulty else 0
            # --- Major match bonus ---
            major_bonus = 0.35 if major and major in department.lower() else 0

            # --- Total hybrid score ---
            total_score = base_score + interest_bonus + major_bonus + difficulty_bonus

            recommendations.append({
                "Course Code": row.get("Course Code", ""),
                "Course Title": row.get("Course Title", ""),
                "Compatibility Score": round(float(total_score), 4),
                "Matched Keywords": list(set(course_keywords) & set(map(str.lower, interests))),
                "Department": department,
                "Difficulty": row.get("Difficulty", ""),
                "Credits": credits,
            })

        sorted_recommendations = sorted(recommendations, key=lambda x: x["Compatibility Score"], reverse=True)
        return sorted_recommendations[:top_n]

    def save_model(self, directory_path):
        joblib.dump(self.vectorizer, f"{directory_path}/vectorizer.joblib")
        joblib.dump(self.course_vectors, f"{directory_path}/course_vectors.joblib")

    def load_model(self, directory_path):
        self.vectorizer = joblib.load(f"{directory_path}/vectorizer.joblib")
        self.course_vectors = joblib.load(f"{directory_path}/course_vectors.joblib")
