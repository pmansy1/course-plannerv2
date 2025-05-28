from django.contrib import admin
from .models import Course, UserProfile, Prerequisite, CourseRecommendation

admin.site.register(Course)
admin.site.register(UserProfile)
admin.site.register(Prerequisite)
admin.site.register(CourseRecommendation)

# Register your models here.
