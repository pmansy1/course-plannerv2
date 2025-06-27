from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    recommend_courses,
    get_available_courses,
    find_path,
    get_course_by_title,
    home_view as home,
    create_user_profile,
    course_search,
    user_profile_view,
    all_courses,
    register_view,
    welcome_new_user_view,
    dashboard_view,
)

urlpatterns = [
    # 🚀 Public Welcome Page
    path("welcome/", welcome_new_user_view, name="welcome_new_user"),

    # 🏠 Home Page
    path("", home, name="home"),

    # 👤 User Profile & Dashboard
    path("dashboard/", dashboard_view, name="dashboard"),
    path("profile/", user_profile_view, name="user_profile"),
    path("create_user_profile/", create_user_profile, name="create_user_profile"),
    path("setup-profile/", create_user_profile, name="setup-profile"),  # alias for redirect

    # 🔍 Course Search
    path("course-search/", course_search, name="course_search"),

    # 📚 Courses API and Pages
    path("courses/<str:title>/", get_course_by_title, name="get_course_by_title"),
    path("all-courses/", all_courses, name="all_courses"),

    # ⭐ Recommendations and Planner
    path("recommend/", recommend_courses, name="recommend_courses"),
    path("available-courses/", get_available_courses, name="available_courses"),
    path("find-path/", find_path, name="find_path"),

    # 🔐 Authentication
    path("accounts/login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
    path("accounts/register/", register_view, name="register"),
]

    