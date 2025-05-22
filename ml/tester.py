from recomended_model.path_planner import path_planner
from recomended_model.path_planner import course_recommender
from recomended_model.path_planner import preprocessing
from recomended_model.user_profile import User_student
import pandas as pd


def main():
    # Load and preprocess data
    with open('/Users/joy/Downloads/course_planner/course-plannerv2/ml/data/courses.csv', 'r') as file:
        # Read the CSV file
        data = file.read()
        print(data)
    course_df = pd.read_csv('/Users/joy/Downloads/course_planner/course-plannerv2/ml/data/courses.csv')
    
    course_df = preprocessing.preprocess_text(course_df, 'description')

    # Initialize and fit the recommender
    recommender = course_recommender.CourseRecommender(course_df)
    recommender.fit()

    # Example user interests
    user_profile = User_student(1, "John Doe", 20, "Computer Science", "Mathematics", 2, 2024, 30, ['CS101', 'CS102'])
    user_profile.add_interest(["machine learning, data science", "artificial intelligence", "deep learning"])
    user_profile.add_interest(user_profile.interests)
    recommendations = recommender.recommend(user_profile.interests)
    print("Recommended Courses:")
    print(recommendations)

    # Initialize path planner
    planner = path_planner.PathPlanner()
    planner.add_prerequisites([('CS101', 'CS102'), ('CS102', 'CS201')])

    # Get available courses based on completed courses
    completed_courses = ['CS101']
    available_courses = planner.get_available_courses(completed_courses)
    print("Available Courses:")
    print(available_courses)

if __name__ == "__main__":
    main()
# This is a test script to demonstrate the functionality of the recommender system and path planner.