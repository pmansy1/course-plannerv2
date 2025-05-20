from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import pickle

class CourseRecommender:
    def __init__(self, course_df: pd.DataFrame):
        self.course_df = course_df
        self.vectorizer = TfidfVectorizer()
        self.course_vectors = None

    def fit(self):
        descriptions = self.course_df['description'].fillna('')
        self.course_vectors = self.vectorizer.fit_transform(descriptions)

    def recommend(self, user_interests, top_n=5):
        if self.course_vectors is None:
            raise Exception("Model not fitted. Call fit() first.")
        user_vec = self.vectorizer.transform([user_interests])
        scores = cosine_similarity(user_vec, self.course_vectors)[0]
        top_indices = scores.argsort()[-top_n:][::-1]
        return self.course_df.iloc[top_indices]

    def save_model(self, path):
        with open(path, 'wb') as f:
            pickle.dump((self.vectorizer, self.course_vectors), f)

    def load_model(self, path):
        with open(path, 'rb') as f:
            self.vectorizer, self.course_vectors = pickle.load(f)
