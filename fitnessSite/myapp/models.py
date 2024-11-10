# myapp/models.py
from django.db import models
from django.contrib.auth.models import User

# Fitness Profile linked to a user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_weight = models.FloatField(default=0)  # Set default value
    goal_weight = models.FloatField(default=0)  # Set default value
    timeline = models.IntegerField(default=0)  # Set default value
    macros = models.CharField(max_length=255, blank=True)

# Exercise Tracking
class Exercise(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    weight = models.FloatField()

