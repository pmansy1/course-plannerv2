import pandas as pd
from course_recommender import CourseRecommender  # your recommender class

def normalize_code(code):
    if not isinstance(code, str):
        return ""
    return code.strip().lower().replace('.', '').replace('-', '').replace(' ', '')

# Load course dataset
course_df = pd.read_csv('final_cleaned_courses_v1.csv')
course_df['Normalized Code'] = course_df['Course Code'].apply(normalize_code)

# Sample student profiles with majors included
student_profiles = [
    {
        "interests": ["machine learning", "data science", "neural networks"],
        "completed_courses": ["CS101", "MATH200"],
        "year": "junior",
        "difficulty_preference": "advanced",
        "major": "computer science"
    },
    {
        "interests": ["writing", "communication", "media"],
        "completed_courses": [],
        "year": "freshman",
        "difficulty_preference": "easy",
        "major": "media studies"
    },
    {
        "interests": ["health", "wellness", "psychology"],
        "completed_courses": ["PSYC1000", "HLTH2000"],
        "year": "senior",
        "difficulty_preference": "medium",
        "major": "health sciences"
    },
]

def normalize_course_list(courses):
    return [normalize_code(c) for c in courses]

def test_recommender_only():
    recommender = CourseRecommender(course_df)
    recommender.fit()

    for idx, profile in enumerate(student_profiles, start=1):
        print(f"\n{'='*10} Profile #{idx} {'='*10}")

        completed_norm = normalize_course_list(profile['completed_courses'])
        profile_data = {
            "interests": " ".join(profile["interests"]),
            "completed_courses": completed_norm,
            "year": profile["year"],
            "difficulty_preference": profile["difficulty_preference"],
            "major": profile["major"]
        }

        recommendations = recommender.recommend(user_profile=profile_data, top_n=5)

        # Filter recommendations to courses that actually exist in the dataset
        filtered_recs = [r for r in recommendations if normalize_code(r.get('Course Code', '')) in set(course_df['Normalized Code'])]

        if not filtered_recs:
            print("⚠️ No suitable recommendations found.")
            continue

        print("🎓 Top 5 Course Recommendations:")
        for rec in filtered_recs[:5]:
            print(f"  {rec.get('Course Code', 'N/A').upper()} | {rec['Course Title']} — Score: {rec['Compatibility Score']}")
            print(f"    Reason: {rec['Recommendation Reason']}")
            print(f"    Matched Keywords: {rec['Matched Keywords']}")

if __name__ == "__main__":
    test_recommender_only()
