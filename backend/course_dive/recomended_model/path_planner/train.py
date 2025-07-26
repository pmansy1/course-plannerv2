import pandas as pd
from path_planner_model import PathPlanner, UserStudent
from course_recommender import CourseRecommender

# Load course data
pamphlet_df = pd.read_csv("/Users/joy/Downloads/preprocessed_courses_high_quality_keywords.csv")
recommender_df = pd.read_csv("/Users/joy/Downloads/course_planner/course-plannerv2/final_cleaned_courses_v1.csv")

# Initialize models
recommender = CourseRecommender(recommender_df)
planner = PathPlanner(recommender_df)

# --- Define student profiles ---
students = [
    UserStudent(
        user_id=1,
        name="Alice",
        age=20,
        major="Computer Science",
        minor="Math",
        year="Sophomore",
        exp_grad_year=2027,
        credits_completed=30,
        completed_courses=["COMP 1010", "COMP 1020"],
        interests=["AI", "machine learning", "software engineering"]
    ),
    UserStudent(
        user_id=2,
        name="Brian",
        age=21,
        major="Marketing",
        minor="Business Analytics",
        year="Junior",
        exp_grad_year=2026,
        credits_completed=60,
        completed_courses=["BUS 2000", "MKTG 2000"],
        interests=["branding", "market research", "advertising"]
    ),
    UserStudent(
        user_id=3,
        name="Carmen",
        age=19,
        major="Psychology",
        minor="Sociology",
        year="Freshman",
        exp_grad_year=2028,
        credits_completed=15,
        completed_courses=["PSYC 1100"],
        interests=["cognitive science", "mental health", "neuroscience"]
    ),
    UserStudent(
        user_id=4,
        name="David",
        age=22,
        major="Biology",
        minor="Chemistry",
        year="Senior",
        exp_grad_year=2025,
        credits_completed=90,
        completed_courses=["BIOL 1200", "CHEM 1200", "BIOL 1300"],
        interests=["genetics", "immunology", "research"]
    ),
    UserStudent(
        user_id=5,
        name="Eva",
        age=20,
        major="Fine Arts",
        minor="Art History",
        year="Sophomore",
        exp_grad_year=2027,
        credits_completed=35,
        completed_courses=["DSGN 1010", "ART 1100"],
        interests=["creativity", "painting", "illustration"]
    ),
]

# --- Test each student ---
for student in students:
    print(f"\n{'='*50}")
    print(f"📚 Student: {student.name} | Major: {student.major}")
    print(f"✅ Completed Courses: {student.completed_courses}")
    print(f"🎨 Interests: {student.interests}")

    try:
        recommender.fit()
        top_courses = recommender.recommend(
            user_profile=student.get_user_profile(),
            top_n=8
        )
    except Exception as e:
        print(f"❌ Failed to get recommendations for {student.name}: {e}")
        continue

    if not top_courses:
        print("⚠️ No recommended courses found.")
        continue

    for target_course in top_courses:
        print(f"\n🎯 Planning path to top course: {target_course}")
        try:
            plan = planner.plan_path(
                completed_courses=student.completed_courses,
                target_course_code=target_course,
                interests=student.interests,
                major=student.major,
            )

            for quarter in ["Fall", "Winter", "Spring"]:
                print(f"\n🗓️ {quarter} Plan:")
                if quarter in plan:
                    for course_code, credits in plan[quarter]:
                        print(f"  - {course_code} ({credits} credits)")
                else:
                    print("  - No courses planned.")
            break  # Stop after first successful path
        except Exception as e:
            print(f"⚠️ Could not plan path to {target_course}: {e}")
            continue