from django.db import models
from django.conf import settings  # Use this instead of importing User directly
from django import forms

# Profile Model
class Profile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    LOOKING_FOR_CHOICES = [
        ('friendship', 'Friendship'),
        ('relationship', 'Relationship'),
        ('networking', 'Networking'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    picture = models.ImageField(
        upload_to='profile_pictures/',
        default='profile_pictures/blank-profile-picture-973460_1280.jpg'
    )
    bio = models.TextField(max_length=500, blank=True)
    interests = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    looking_for = models.CharField(max_length=20, choices=LOOKING_FOR_CHOICES, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

# Message Model
class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender.username} to {self.recipient.username}'

# Match Model
class Match(models.Model):
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='matches_initiated', on_delete=models.CASCADE)
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='matches_received', on_delete=models.CASCADE)
    matched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Match: {self.user1.username} & {self.user2.username}'

# Forms remain the same
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture', 'bio', 'interests', 'location', 'date_of_birth', 'gender', 'looking_for']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Tell us about yourself...'}),
            'interests': forms.Textarea(attrs={'rows': 3, 'placeholder': 'What are your hobbies and interests?'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter your city or region'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'looking_for': forms.Select(attrs={'class': 'form-control'}),
        }

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your message...'}),
        }
