from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    #instructor = models.CharField(max_length=255)
    credit_hours = models.IntegerField()  # credit hours
    level = models.CharField(max_length=50)  # Beginner, Intermediate, Advanced
    keywords = models.TextField(blank=True) #keywords for search
    prerequisites_txt = models.ManyToManyField('self', symmetrical=False, blank=True)

    
    def __str__(self):
        return self.title
    
    def get_prerequisites(self):
        return self.prerequisites.split(',') if self.prerequisites else []
    
    def get_keywords(self):
        return self.keywords.split(',') if self.keywords else []
class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    major = models.CharField(max_length=100)
    minor = models.CharField(max_length=100, blank=True, null=True)
    year = models.CharField(max_length=50)  # Freshman, Sophomore, etc.
    exp_grad_year = models.IntegerField()
    credits_completed = models.IntegerField()
    completed_courses = models.ManyToManyField(Course, related_name='completed_by')
    interests = interests = models.TextField()


    def __str__(self):
        return f"{self.user.username}'s Profile"


class Prerequisite(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="prerequisite_links")

    def __str__(self):
        return f"{self.prerequisite_course.title} is a prerequisite for {self.course.title}"