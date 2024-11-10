# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import RegisterForm, ProfileForm
from .models import Profile, Exercise, Progress


# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in if authentication succeeds
            login(request, user)
            return HttpResponseRedirect(reverse('profile'))  # Redirect to profile after successful login
        else:
            # If authentication fails, send an error message to the template
            return render(request, 'myapp/login.html', {'error': 'Invalid username or password'})

    # Render the login page if it's a GET request
    return render(request, 'myapp/login.html')


# Register view
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, current_weight=0, goal_weight=0,
                                   timeline=0)  # Create profile with default values
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'myapp/register.html', {'form': form})


# Profile page (handles profile data and macros)
@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile.current_weight = form.cleaned_data['current_weight']
            profile.goal_weight = form.cleaned_data['goal_weight']
            profile.timeline = form.cleaned_data['timeline']
            # Calculate macros based on form input and update profile
            profile.macros = calculate_macros(profile.current_weight, profile.goal_weight, profile.timeline)
            profile.save()
    else:
        form = ProfileForm()
    return render(request, 'myapp/profile.html', {'form': form, 'profile': profile})


# Macro calculation helper function
def calculate_macros(current_weight, goal_weight, timeline):
    # Example calculation logic
    return f"Calories: {current_weight * 10}, Protein: {current_weight * 0.8}g"


# Exercises page
def exercises(request):
    exercises = [
        {'name': 'Push-up', 'description': 'An exercise to strengthen the chest, shoulders, and triceps.'},
        {'name': 'Squat', 'description': 'An exercise for the lower body, especially quads and glutes.'}
    ]
    return render(request, 'myapp/exercises.html', {'exercises': exercises})


# Progress tracking page
@login_required
def tracking(request):
    dates = ["Jan", "Feb", "Mar"]  # Replace with real data
    weights = [150, 145, 140]  # Replace with real data
    return render(request, 'myapp/tracking.html', {'dates': dates, 'weights': weights})


# Recipe ideas page
def recipes(request):
    recipes = [
        {'name': 'Avocado Toast', 'description': 'A quick breakfast with healthy fats and fiber.'},
        {'name': 'Chicken Salad', 'description': 'High-protein meal with vegetables and lean protein.'}
    ]
    return render(request, 'myapp/recipes.html', {'recipes': recipes})
