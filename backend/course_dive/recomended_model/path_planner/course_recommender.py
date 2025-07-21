from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from keyword_cleaner import clean_keywords
class CourseRecommender:
    def __init__(self, course_df):
        self.course_df = course_df.copy()
        self.vectorizer = TfidfVectorizer()
        self.course_vectors = None

        # Clean keywords column for vectorizer input
        if 'Keywords' in self.course_df.columns:
            self.course_df['cleaned_keywords'] = self.course_df['Keywords'].fillna('').apply(clean_keywords)
        else:
            self.course_df['cleaned_keywords'] = ''

        # Add major-related keywords column if not exists
        if 'Major Keywords' not in self.course_df.columns:
            # Could be empty or derived later
            self.course_df['Major Keywords'] = ''

    def fit(self):
        # Vectorize cleaned keywords + major keywords combined
        combined_text = self.course_df['cleaned_keywords'] + " " + self.course_df['Major Keywords'].fillna('')
        self.course_vectors = self.vectorizer.fit_transform(combined_text)

    def recommend(self, user_profile, top_n=5):
        user_interests = user_profile.get('interests', '')
        completed_courses = set([c.lower() for c in user_profile.get('completed_courses', [])])
        user_major = user_profile.get('major', '').lower()

        # Format interests string
        if isinstance(user_interests, list):
            user_interests = " ".join(user_interests)

        # Include major as weighted keyword boost in user vector
        # Repeat major keywords multiple times to increase weight
        major_keywords = " ".join([user_major]*5) if user_major else ""
        combined_user_text = user_interests + " " + major_keywords

        user_vec = self.vectorizer.transform([combined_user_text])
        similarity_scores = cosine_similarity(user_vec, self.course_vectors)[0]

        recommendations = []

        for i, row in self.course_df.iterrows():
            # Skip courses already completed
            course_code = str(row.get('Course Code', '')).lower()
            if course_code in completed_courses:
                continue

            score = similarity_scores[i] * 100  # scale

            # Bonus for major match: if course 'Major Keywords' contain user major, boost score
            course_major_keywords = row.get('Major Keywords', '').lower()
            if user_major and user_major in course_major_keywords:
                score += 15  # tuning parameter for boost

            # Bonus if difficulty matches user preference (if you have difficulty info)
            difficulty = user_profile.get('difficulty_preference', '').lower()
            if difficulty and difficulty in row.get('cleaned_keywords', ''):
                score += 5

            if score > 0:
                reason_parts = []
                if user_major and user_major in course_major_keywords:
                    reason_parts.append(f"Related to your major: {user_major}")
                reason_parts.append("Matched with your interests")
                recommendations.append({
                    "Course Title": row['Course Title'],
                    "Course Code": row['Course Code'],
                    "Compatibility Score": round(score, 2),
                    "Matched Keywords": row['cleaned_keywords'],
                    "Recommendation Reason": "; ".join(reason_parts)
                })

        # Sort top scoring courses only
        recommendations = sorted(recommendations, key=lambda x: x['Compatibility Score'], reverse=True)
        return recommendations[:top_n]
