from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from ..user_profile import User_student
import pickle

class CourseRecommender:
    def __init__(self, course_df: pd.DataFrame, user_profile: User_student = None):
        self.course_df = course_df
        self.user_profile = user_profile
        self.vectorizer = TfidfVectorizer()
        self.course_vectors = None

    def fit(self):
        if 'keywords' in self.course_df.columns:
            texts = self.course_df['keywords'].fillna('')
        else:
            texts = self.course_df['description'].fillna('')
        self.course_vectors = self.vectorizer.fit_transform(texts)

    def recommend(self, user_interests, top_n=5):
        if self.course_vectors is None:
            raise Exception("Model not fitted. Call fit() first.")
        if user_interests is None:
            if self.user_profile is None:
                raise ValueError("No user profile or interests provided.")

        user_vec = self.vectorizer.transform([user_interests])
        scores = cosine_similarity(user_vec, self.course_vectors)[0]
        top_indices = scores.argsort()[-top_n:][::-1]

        # Slice top courses and add similarity column
        top_courses = self.course_df.iloc[top_indices].copy()
        top_courses['similarity'] = scores[top_indices]
        return top_courses

    def save_model(self, path):
        with open(path, 'wb') as f:
            pickle.dump((self.vectorizer, self.course_vectors), f)

    def load_model(self, path):
        with open(path, 'rb') as f:
            self.vectorizer, self.course_vectors = pickle.load(f)
