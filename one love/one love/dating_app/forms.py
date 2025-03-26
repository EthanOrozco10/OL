from django import forms
from .models import Profile, Message

# Profile Update Form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture', 'bio', 'interests', 'location', 'date_of_birth', 'gender', 'looking_for']
        widgets = {
            'bio': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Tell us about yourself...',
                'class': 'form-control',
            }),
            'interests': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'What are your hobbies and interests?',
                'class': 'form-control',
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'Enter your city or region',
                'class': 'form-control',
            }),
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control',
            }),
            'looking_for': forms.Select(attrs={
                'class': 'form-control',
            }),
        }

# Profile Picture Update Form
class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture']
        widgets = {
            'picture': forms.FileInput(attrs={
                'class': 'form-control-file',
            }),
        }

# Message Form for Chat Feature
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your message...',
                'class': 'form-control',
            }),
        }
