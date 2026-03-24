from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    profile_picture = models.URLField(blank=True)  # placeholder: stores image URL
    reputation_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} profile"
