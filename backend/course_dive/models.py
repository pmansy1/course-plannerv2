from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.CharField(max_length=255, blank=True)  # optional field for instructor name
    credit_hours = models.IntegerField()  # credit hours
    level = models.CharField(max_length=50)  # Beginner, Intermediate, Advanced
    keywords = models.TextField(blank=True) #keywords for search
    prerequisites = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.title
    
    def get_prerequisites(self):
        return [course.title for course in self.prerequisites.all()]
    
    def get_keywords(self):
        return self.keywords.split(',') if self.keywords else []

class User(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class CourseRecommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommended_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    recommendation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recommendation for {self.user.username}: {self.recommended_course.title}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    first_name = models.CharField(max_length=30, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    major = models.CharField(max_length=100, null=True, blank=True)
    minor = models.CharField(max_length=100, blank=True, null=True)
    year = models.CharField(max_length=50)  # Freshman, Sophomore, etc.
    difficulty_preference = models.CharField(max_length=20, blank=True, null=True)  # Difficulty preference
    exp_grad_year = models.IntegerField(null=True, blank=True)  # Expected graduation year
    credits_completed = models.IntegerField(null=True, blank=True)  # Number of credits completed
    completed_courses = models.ManyToManyField(Course, related_name='completed_by', blank=True)
    interests = interests = models.TextField(null=True, blank=True)  # Comma-separated interests

    @property
    def is_profile_complete(self):
        required_fields = [
            self.age, self.major, self.year,
            self.exp_grad_year, self.credits_completed, self.interests
        ]
        return all(required_fields)
    def __str__(self):
        return f"{self.user.username}'s Profile"


class Prerequisite(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="prerequisite_links")

    def __str__(self):
        return f"{self.prerequisite_course.title} is a prerequisite for {self.course.title}"
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)