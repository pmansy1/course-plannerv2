from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from django import forms
from .models import UserProfile

User = get_user_model()
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'first_name',
            'age',
            'major',
            'minor',
            'year',
            'difficulty_preference',
            'exp_grad_year',
            'credits_completed',
            'completed_courses',
            'interests',
        ]
        widgets = {
            'interests': forms.Textarea(attrs={'rows': 3}),
        }
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 17:
            raise forms.ValidationError("You must be at least 17 years old.")
        return age



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
    
