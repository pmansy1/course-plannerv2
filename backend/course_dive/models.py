from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Course(models.Model):
    crn = models.CharField(max_length=10, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="No description provided.")
    credit_hours = models.IntegerField(default=0)
    level = models.CharField(max_length=50, default="Unknown")
    keywords = models.TextField(blank=True, default="No keywords")
    instructor = models.CharField(max_length=255, default='TBD')
    department = models.CharField(max_length=100, default="General")

    def __str__(self):
        return self.title

    def get_prerequisites(self):
        """
        Returns a list of prerequisite course titles and/or notes.
        """
        prereqs = []
        for p in self.prerequisites.all():
            if p.prerequisite_course:
                prereqs.append(p.prerequisite_course.title)
            elif p.note:
                prereqs.append(f"Note: {p.note}")
        return prereqs

    def get_keywords(self):
        return [kw.strip().lower() for kw in self.keywords.split(',') if kw.strip()]

# =======================
# User Model
# =======================
class User(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

# =======================
# Course Recommendation Model
# =======================
class CourseRecommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommended_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    compatibility_score = models.IntegerField(default=0)
    matched_keywords = models.TextField(blank=True, null=True)  # comma-separated
    recommendation_reason = models.TextField(blank=True, null=True)
    recommendation_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Recommendation for {self.user.username}: {self.recommended_course.title}"

# =======================
# User Profile Model
# =======================
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    first_name = models.CharField(max_length=30, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    major = models.CharField(max_length=100, null=True, blank=True)
    minor = models.CharField(max_length=100, null=True, blank=True)
    year = models.CharField(max_length=50)  # Freshman, Sophomore, etc.
    difficulty_preference = models.CharField(max_length=20, blank=True, null=True)
    exp_grad_year = models.IntegerField(null=True, blank=True)
    credits_completed = models.IntegerField(null=True, blank=True)
    completed_courses = models.ManyToManyField(Course, related_name='completed_by', blank=True)
    interests = models.TextField(null=True, blank=True)  # Comma-separated interests
    SCHEDULE_CHOICES = [
    ('semester', 'Semester'),
    ('quarter', 'Quarter'),
    ]

    schedule_type = models.CharField(
    max_length=10,
    choices=SCHEDULE_CHOICES,
    default='semester',
)

    @property
    def is_profile_complete(self):
        required_fields = [
            self.age, self.major, self.year,
            self.exp_grad_year, self.credits_completed, self.interests
        ]
        return all(required_fields)

    def __str__(self):
        return f"{self.user.username}'s Profile"

# =======================
# Prerequisite Model
# =======================
class Prerequisite(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='prerequisites')
    prerequisite_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='prerequisite_for', null=True, blank=True)
    note = models.CharField(max_length=255, blank=True, null=True)  # For notes if course not found

    def __str__(self):
        if self.prerequisite_course:
            return f"{self.course.title} prerequisite: {self.prerequisite_course.title}"
        elif self.note:
            return f"{self.course.title} requires note: {self.note}"
        else:
            return f"{self.course.title} has no prerequisites"

# =======================
# User Profile Creation Signal
# =======================
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)