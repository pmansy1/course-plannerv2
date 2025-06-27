from django.shortcuts import render, redirect
from .recomended_model.path_planner.course_recommender import CourseRecommender
from .recomended_model.path_planner.path_planner import PathPlanner
from .recomended_model.user_profile import User_student
from .models import Course, User, UserProfile, CourseRecommendation
import pandas as pd
import ast
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import CustomUserCreationForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth import login

def home_view(request):
    if request.user.is_authenticated:
        if not hasattr(request.user, 'userprofile'):
            return redirect('create_user_profile')
        return redirect('dashboard')
    return render(request, 'home.html')

@login_required
def user_profile_view(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        return redirect('create_user_profile')

    completed_courses = user_profile.completed_courses.all()

    context = {
        'user': user_profile.user,
        'profile': user_profile,
        'completed_courses': completed_courses,
    }

    return render(request, 'user_profile.html', context)

@login_required
def recommend_courses(request):
    user_profile = request.user.userprofile
    interests = user_profile.interests

    course_qs = Course.objects.all().values('title', 'description', 'keywords', 'prerequisites')
    course_df = pd.DataFrame.from_records(course_qs)

    recommender = CourseRecommender(course_df, user_profile)
    recommender.fit()
    recommended_df = recommender.recommend(interests)

    recommendations = recommended_df.to_dict('records')
    return render(request, 'recommendations.html', {'courses': recommendations})

@login_required
def get_available_courses(request):
    user_profile = request.user.userprofile
    completed_courses = user_profile.completed_courses.all()
    completed_course_titles = [course.title for course in completed_courses]

    course_qs = Course.objects.all().values('title', 'description', 'keywords', 'prerequisites')
    course_df = pd.DataFrame.from_records(course_qs)

    recommender = CourseRecommender(course_df)
    recommender.fit()
    available_courses = recommender.get_available_courses(completed_course_titles)

    available_courses_list = [{'title': course} for course in available_courses]
    return JsonResponse(available_courses_list, safe=False)

def course_search(request):
    query = request.GET.get('q', '').strip()
    results = []

    if query:
        results = Course.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(keywords__icontains=query)
        )

    return render(request, 'search_results.html', {
        'query': query,
        'results': results
    })

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

@login_required
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
            prerequisites = ast.literal_eval(prerequisites)
        for prereq in prerequisites:
            prereq_pairs.append((prereq, course_title))

    path_planner = PathPlanner()
    path_planner.add_prerequisites(prereq_pairs)

    end_course = request.GET.get('end_course')
    paths = path_planner.find_path(completed_course_titles, end_course)
    return JsonResponse(paths, safe=False)

@login_required
def save_course_recommendation(request):
    if request.method == 'POST':
        user = request.user
        course_title = request.POST.get('course_title')
        course = Course.objects.filter(title=course_title).first()

        if not course:
            return JsonResponse({'error': 'Course not found'}, status=404)

        recommendation, created = CourseRecommendation.objects.get_or_create(
            user=user,
            course=course,
            defaults={'reason': request.POST.get('reason', '')}
        )

        if not created:
            recommendation.reason = request.POST.get('reason', '')
            recommendation.save()

        return JsonResponse({'message': 'Course recommendation saved successfully'})
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)  # Automatically create UserProfile
            login(request, user)
            messages.success(request, 'Account created successfully.')
            return redirect('create_user_profile')
        else:
            messages.error(request, 'There was a problem with your registration.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def create_user_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'create_user_profile.html', {'form': form})

def all_courses(request):  
    courses = Course.objects.all()
    return render(request, 'all_courses.html', {'courses': courses})

def welcome_new_user_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'welcome_new_user.html')

@login_required
def dashboard_view(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        return redirect('create_user_profile')

    context = {
        'profile': user_profile,
        'next_steps': [
            {'label': 'Search Courses', 'url': '/course-search/'},
            {'label': 'View Recommendations', 'url': '/recommend/'},
            {'label': 'Explore All Courses', 'url': '/all-courses/'},
        ]
    }
    return render(request, 'dashboard.html', context)