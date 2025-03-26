from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'gender', 'looking_for')  # Customize columns displayed in the admin list view
    search_fields = ('user__username', 'location', 'interests')  # Add search functionality
    list_filter = ('gender', 'looking_for', 'location')  # Add filters for better admin panel usability
    ordering = ('user',)  # Default ordering by user
