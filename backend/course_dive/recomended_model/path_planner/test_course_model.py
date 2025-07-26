import pandas as pd
from course_recommender import CourseRecommender
import joblib
import os

def run_test(user_profile, label, recommender, df):
    print(f"\n=== {label} ===")
    recommender.fit()  # Ensure recommender is trained
    recommendations = recommender.recommend(user_profile, top_n=10)
    if not recommendations:
        print("No recommendations found.\n")
        return
    for rec in recommendations:
        course_code = rec['Course Code']
        course_title = rec['Course Title']
        score = rec['Compatibility Score']
        matched_keywords = rec.get('keywords', [])
        matched_row = df[df['Course Code'] == course_code]
        if not matched_row.empty:
            difficulty = matched_row['Difficulty'].values[0]
            credits = matched_row['Credits'].values[0]
        else:
            difficulty = "Unknown"
            credits = "Unknown"
        print(f"  {course_code}: {course_title}  ({score}) | Keywords: {matched_keywords} | Difficulty: {difficulty}")

# Load course data
course_path = "/Users/joy/Downloads/course_planner/course-plannerv2/final_cleaned_courses_v1.csv"
df = pd.read_csv(course_path)

# Normalize course codes if needed (optional)
def normalize_code(code):
    if not isinstance(code, str):
        return ""
    return code.strip().lower().replace('.', '').replace('-', '').replace(' ', '')
df['Normalized Code'] = df['Course Code'].apply(normalize_code)

# Create recommender instance
recommender = CourseRecommender(df)
# No explicit fit() needed if your class does vectorizer in __init__

# Diverse student profiles
students = {
    "STEM Freshman": {
        "interests": ["math", "programming", "algorithms", "physics"],
        "major": "computer science",
        "year": "Freshman",
        "difficulty": "beginner",
        "completed_courses": []
    },
    "Humanities Sophomore": {
        "interests": ["history", "philosophy", "writing", "politics"],
        "major": "history",
        "year": "Sophomore",
        "difficulty": "intermediate",
        "completed_courses": []
    },
    "Business Junior": {
        "interests": ["entrepreneurship", "finance", "marketing", "strategy"],
        "major": "business",
        "year": "Junior",
        "difficulty": "intermediate",
        "completed_courses": []
    },
    "Pre-Med Senior": {
        "interests": ["biology", "chemistry", "anatomy", "health"],
        "major": "biology",
        "year": "Senior",
        "difficulty": "advanced",
        "completed_courses": []
    },
    "Art Major": {
        "interests": ["painting", "design", "creativity", "sculpture"],
        "major": "Art",
        "year": "Sophomore",
        "difficulty": "flexible",
        "completed_courses": []
    }
}

# Run tests on these profiles
for label, profile in students.items():
    run_test(profile, label, recommender, df)

# Optional: test a specific profile
test_profile = {
    "interests": ["data science", "machine learning", "statistics"],
    "completed_courses": ["cs101", "math200"],
    "year": "Junior",
    "difficulty": "advanced",
    "major": "computer science"
}
run_test(test_profile, "Test User Profile", recommender, df)

# Save the model if needed
recommender.save_model("saved_models")
