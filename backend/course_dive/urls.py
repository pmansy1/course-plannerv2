from django.urls import path
from .views import (
    recommend_courses,
    get_available_courses,
    find_path,
    get_all_courses,
    get_course_by_title,
    home,
    create_user_profile,
)
    



urlpatterns = [
    path("", home, name="home"),
    path('recommend/', recommend_courses, name='recommend_courses'),
    path('available_courses/', get_available_courses, name='available_courses'),
    path('find_path/', find_path, name='find_path'),
    path('courses/', get_all_courses, name='courses'),
    path('courses/<str:title>/', get_course_by_title, name='get_course_by_title'),
    path('create_user_profile/', create_user_profile, name='create_user_profile'),
]