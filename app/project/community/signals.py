from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver

from tennis import models as TennisModels

from . import models
from .utils import check_achievement


@receiver(post_save, sender=TennisModels.TennisSession)
def check_tennis_session_achievements(sender, instance, **kwargs):
    user = instance.user
    # Checking the number of completed tennis sessions achievements.
    check_achievement(user,
                      "Tennis Sessions",
                      "Tennis Sessions",
                      [1, 5, 25, 50, 100])

    # Achievement Categories related to tennis sessions.
    categories = ["Backhand Sessions", "Forehand Sessions", "Serve Sessions",
                  "Volley Sessions", "Slice Sessions", "Smash Sessions",
                  "Drop-Shot Sessions", "Agility Sessions", "Stamina Sessions"]

    for category in categories:
        check_achievement(user,
                          category,
                          category,
                          [5, 10, 25, 50, 100])


@receiver(post_save, sender=models.UserPosts)
def check_posts_achievements(sender, instance, **kwargs):
    user = instance.user_profile.user
    # Checking the number of created posts achievements.
    check_achievement(user,
                      "Created Posts",
                      "Created Posts",
                      [1, 5, 10, 15, 20, 25])


@receiver(post_save, sender=models.Like)
def check_likes_achievements(sender, instance, **kwargs):
    user = instance.user_profile.user
    # Checking the number of given likes achievements.
    check_achievement(user,
                      "Liked Posts",
                      "Liked Posts",
                      [5, 10, 25, 50, 100])


@receiver(post_save, sender=models.Comment)
def check_comments_achievements(sender, instance, **kwargs):
    user = instance.user_profile.user
    # Checking the number of given comments achievements.
    check_achievement(user,
                      "Comment Count",
                      "Comment Count",
                      [1, 5, 10, 15, 20, 25])


@receiver(post_save, sender=models.Follow)
def check_follow_achievements(sender, instance, **kwargs):
    user = instance.followed_by.user
    # Checking the followed count achievements.
    check_achievement(user,
                      "Followed Count",
                      "Followed Count",
                      [1, 2, 5, 10])

    # Checking the followers count achievements.
    check_achievement(user,
                      "Followers Count",
                      "Followers Count",
                      [1, 2, 5, 10])
