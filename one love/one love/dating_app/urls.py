from django.urls import path
from django.contrib.auth.views import LogoutView  # Import LogoutView
from . import views

urlpatterns = [
    # Home and Authentication
    path('', views.home, name='home'),
    path('signup/', views.register, name='signup'),  # Changed URL from 'register' to 'signup'
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),  # Use LogoutView for logout

    # Profile Management
    path('browse_profiles/', views.browse_profiles, name='browse_profiles'),
    path('profile/<int:profile_id>/', views.view_profile, name='view_profile'),  # View a specific profile
    path('edit_profile/', views.edit_profile, name='edit_profile'),  # Edit the logged-in user's profile
    path('upload_picture/', views.upload_profile_picture, name='upload_profile_picture'),  # Upload profile picture

    # Matching
    path('match_profiles/', views.match_profiles, name='match_profiles'),  # Match with another user

    # Messaging
    path('messages/', views.messages, name='messages'),  # Placeholder for messages

    # Settings
    path('settings/', views.settings, name='settings'),
    path('profile_settings/', views.profile_settings, name='profile_settings'),  # Manage profile settings
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('chat/', views.chat, name='chat'),
    path('matches/', views.match_profiles, name='matches'),

]
