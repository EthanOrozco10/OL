from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Automatically create a Profile for new Users
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            bio="This is your bio! Share something about yourself.",
            interests="Add your interests here.",
            location="Update your location."
        )

# Save the User's Profile when the User is updated
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
