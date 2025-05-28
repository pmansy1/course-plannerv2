from django.shortcuts import render
from .recomended_model.path_planner.course_recommender import CourseRecommender
from .recomended_model.path_planner.path_planner import PathPlanner
from .recomended_model.user_profile import User_student
from .models import Course, User, UserProfile, CourseRecommendation
import pandas as pd
import ast
from django.http import JsonResponse

# Create your views here.

def recommend_courses(request):
    user_profile = request.user.userprofile
    interests = user_profile.interests

    course_qs = Course.objects.all().values('title', 'description', 'keywords', 'prerequisites')
    course_df = pd.DataFrame.from_records(course_qs)

    recommender = CourseRecommender(course_df, user_profile)
    recommender.fit()
    recommended_df = recommender.recommend(interests)

    # Convert to list of dicts to render in template
    recommendations = recommended_df.to_dict('records')

    return render(request, 'recommendations.html', {'courses': recommendations})

def get_available_courses(request):
    user_profile = request.user.userprofile
    completed_courses = user_profile.completed_courses.all()
    completed_course_titles = [course.title for course in completed_courses]

    course_qs = Course.objects.all().values('title', 'description', 'keywords', 'prerequisites')
    course_df = pd.DataFrame.from_records(course_qs)

    recommender = CourseRecommender(course_df)
    recommender.fit()
    available_courses = recommender.get_available_courses(completed_course_titles)

    # Convert to list of dicts to render in template
    available_courses_list = [{'title': course} for course in available_courses]

    return JsonResponse(available_courses_list, safe=False)

def get_all_courses(request):
    courses = Course.objects.all().values('title', 'description', 'keywords')
    return JsonResponse(list(courses), safe=False)

def get_course_by_title(request, title):
    try:
        course = Course.objects.get(title=title)
        return JsonResponse({
            'title': course.title,
            'description': course.description,
            'keywords': course.keywords,
        })
    except Course.DoesNotExist:
        return JsonResponse({'error': 'Course not found'}, status=404)

def find_path(request):
    user_profile = request.user.userprofile
    completed_courses = user_profile.completed_courses.all()
    completed_course_titles = [course.title for course in completed_courses]

    course_qs = Course.objects.all()
    course_df = pd.DataFrame.from_records(course_qs)
    prereq_pairs = []

    for course in Course.objects.all():
        for prereq in course.get_prerequisites():
            prereq_pairs.append((course.title, prereq))
    for _, row in course_df.iterrows():
        course_title = row['title']
        prerequisites = row.get('prerequisites', [])

        if isinstance(prerequisites, str):
            # Convert stringified lists from DB if needed
            prerequisites = ast.literal_eval(prerequisites)

        for prereq in prerequisites:
            prereq_pairs.append((prereq, course_title))
    path_planner = PathPlanner()
    path_planner.add_prerequisites(prereq_pairs)

    start_courses = completed_course_titles
    end_course = request.GET.get('end_course')

    paths = path_planner.find_path(start_courses, end_course)
    
    return JsonResponse(paths, safe=False)

