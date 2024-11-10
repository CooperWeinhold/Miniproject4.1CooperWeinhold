# myapp/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# User Registration Form (customize fields if needed)
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# Profile Form for Fitness Goals
class ProfileForm(forms.Form):
    current_weight = forms.FloatField(label='Current Weight (lbs)')
    goal_weight = forms.FloatField(label='Goal Weight (lbs)')
    timeline = forms.IntegerField(label='Timeline (weeks)')
