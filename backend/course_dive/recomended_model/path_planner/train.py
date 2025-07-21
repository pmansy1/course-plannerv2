import pandas as pd
from course_recommender import CourseRecommender
from path_planner import PathPlanner

def normalize_code(code):
    if not isinstance(code, str):
        return ""
    return code.strip().lower().replace('.', '').replace('-', '').replace(' ', '')

# Load course data
course_df = pd.read_csv('final_cleaned_courses_v1.csv')
course_df['Normalized Code'] = course_df['Course Code'].apply(normalize_code)

# Build prerequisite edges for PathPlanner
prereq_edges = []
for _, row in course_df.iterrows():
    course_code = normalize_code(row['Course Code'])
    if pd.notna(row['Prerequisites']):
        prereqs = [normalize_code(pr) for pr in row['Prerequisites'].split(',') if pr.strip()]
        for pr in prereqs:
            prereq_edges.append((pr, course_code))

planner = PathPlanner()
planner.add_prerequisites(prereq_edges)

student_profiles = [
    {
        "interests": ["machine learning", "data science", "neural networks"],
        "completed_courses": ["CS101", "MATH200"],
        "year": "junior",
        "difficulty_preference": "advanced",
        "major": "computer science",
        "desired_credits": 12
    },
    {
        "interests": ["writing", "communication", "media"],
        "completed_courses": [],
        "year": "freshman",
        "difficulty_preference": "easy",
        "major": "media studies",
        "desired_credits": 9
    },
    {
        "interests": ["health", "wellness", "psychology"],
        "completed_courses": ["PSYC1000", "HLTH2000"],
        "year": "senior",
        "difficulty_preference": "medium",
        "major": "health sciences",
        "desired_credits": 6
    },
]

def generate_study_plan(completed, recommended_courses, desired_credits):
    plan = []
    total_credits = 0

    def get_credits(credit_str):
        try:
            s = str(credit_str).lower()
            digits = ''.join(ch for ch in s if ch.isdigit())
            return int(digits) if digits else 0
        except:
            return 0

    for course in recommended_courses:
        ccode = normalize_code(course.get('Course Code', ''))
        if ccode not in plan:
            credits = get_credits(course.get('Credits', '4'))
            plan.append((course['Course Title'], ccode, credits))
            total_credits += credits
            if total_credits >= desired_credits:
                break

    # Filler courses if needed
    if total_credits < desired_credits:
        for _, row in course_df.iterrows():
            ccode = normalize_code(row['Course Code'])
            if ccode not in plan and ccode not in completed:
                credits = get_credits(row['Credits'])
                if credits == 0:
                    credits = 4
                plan.append((row['Course Title'], ccode, credits))
                total_credits += credits
                if total_credits >= desired_credits:
                    break

    return plan

def test_recommender_and_planner():
    for idx, profile in enumerate(student_profiles, start=1):
        print(f"\n{'='*10} Profile #{idx} {'='*10}")

        completed_norm = [normalize_code(c) for c in profile['completed_courses']]
        eligible_courses = planner.get_available_courses(completed_norm)
        print(f"Completed courses (normalized): {completed_norm}")
        print(f"Eligible courses found: {len(eligible_courses)}")

        if not eligible_courses:
            print("⚠️ No eligible courses found for this profile.")
            continue

        eligible_df = course_df[course_df['Normalized Code'].isin(eligible_courses)].copy()

        user_profile = {
            "interests": " ".join(profile['interests']),
            "completed_courses": completed_norm,
            "year": profile['year'],
            "difficulty_preference": profile['difficulty_preference'],
            "major": profile['major']
        }

        recommender_sub = CourseRecommender(eligible_df)
        recommender_sub.fit()
        recommendations = recommender_sub.recommend(user_profile=user_profile, top_n=10)

        # Filter recommendations to ensure valid courses only
        recommendations = [r for r in recommendations if normalize_code(r.get('Course Code', '')) in eligible_courses]

        if not recommendations:
            print("⚠️ No suitable recommendations found.")
            continue

        top_recommendations = recommendations[:5]
        print("\n🎓 Top Course Recommendations:")
        for r in top_recommendations:
            print(f"  {r.get('Course Code', 'N/A').upper()} | {r['Course Title']} — Score: {r['Compatibility Score']}")
            print(f"    Reason: {r['Recommendation Reason']}")
            print(f"    Matched Keywords: {r['Matched Keywords']}")

        study_plan = generate_study_plan(completed_norm, top_recommendations, profile.get('desired_credits', 12))

        print("\n🗓️ Suggested Study Plan:")
        total_credits = 0
        for title, code, credits in study_plan:
            total_credits += credits
            print(f"  - {code.upper()}: {title} ({credits} credits)")
        print(f"Total credits planned: {total_credits}")

        # Path to top recommended course
        top_course_code = normalize_code(top_recommendations[0].get('Course Code', ''))
        path = planner.find_path(completed_norm, top_course_code)
        print("\n🧭 Path to top recommended course:")
        if isinstance(path, dict) and "error" in path:
            print("⚠️", path["error"])
        else:
            print(" → ".join(path[0]))

if __name__ == "__main__":
    test_recommender_and_planner()
