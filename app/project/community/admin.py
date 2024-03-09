from django.contrib import admin
from .models import UserProfile, UserPosts, Achievement, AchievementCategory

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserPosts)
admin.site.register(AchievementCategory)
admin.site.register(Achievement)
