from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Match
from .forms import ProfilePictureForm, ProfileUpdateForm
import random

# Home Page
def home(request):
    return render(request, 'base.html')  # Render the home page template

# User Registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# User Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('browse_profiles')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    return render(request, 'login.html')

# Browse Profiles
@login_required
def browse_profiles(request):
    profiles = Profile.objects.exclude(user=request.user)  # Exclude the logged-in user's profile
    return render(request, 'browse_profiles.html', {'profiles': profiles})

# View Profile
@login_required
def view_profile(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    return render(request, 'view_profile.html', {'profile': profile})

# Edit Profile
@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile', profile_id=profile.id)
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})

# Upload Profile Picture
@login_required
def upload_profile_picture(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('edit_profile')
    else:
        form = ProfilePictureForm(instance=profile)
    return render(request, 'upload_profile_picture.html', {'form': form})

# Match Profiles
@login_required
def match_profiles(request):
    potential_matches = Profile.objects.exclude(user=request.user)
    random_match = random.choice(potential_matches) if potential_matches.exists() else None

    if random_match:
        # Create a match (optional functionality)
        Match.objects.create(user1=request.user, user2=random_match.user)
    
    return render(request, 'match_profiles.html', {'match': random_match})

# Messages
@login_required
def messages(request):
    # Add logic for retrieving and displaying messages
    return render(request, 'messages.html')

# Settings
@login_required
def settings(request):
    return render(request, 'settings.html')

# Profile Settings
@login_required
def profile_settings(request):
    profile = request.user.profile  # Access the profile of the logged-in user
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_settings')  # Redirect after successful update
    else:
        form = ProfilePictureForm(instance=profile)
    return render(request, 'settings.html', {'form': form, 'profile': profile})

# Dashboard View
@login_required
def dashboard(request):
    # For demonstration, we'll just render a 'dashboard.html' template.
    return render(request, 'dashboard.html')

# Chat View
@login_required
def chat(request):
    # Render the chat page template
    return render(request, 'chat.html')
