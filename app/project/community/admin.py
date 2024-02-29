from django.contrib import admin
from .models import UserProfile, UserPosts

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserPosts)
