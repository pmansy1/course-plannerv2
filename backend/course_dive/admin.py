from django.contrib import admin
from .models import Course, UserProfile, CourseRecommendation

admin.site.register(Course)
admin.site.register(UserProfile)
admin.site.register(CourseRecommendation)

# Register your models here.
