from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.


class UserProfile(models.Model):
    """"""
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        default='./community/images/profile-pic-temp.png'
    )
    bio = models.TextField(blank=True)
    username = models.CharField(max_length=50)
    profile_name = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class UserPosts(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post_picture = models.ImageField(
        upload_to='post_pics/'
    )
    post_caption = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.user.username}'s post - {self.created_at}"
