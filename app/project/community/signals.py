from django.db.models.signals import post_save
from django.dispatch import receiver

from tennis import models as TennisModels

from . import models


@receiver(post_save, sender=TennisModels.TennisSession)
def check_tennis_session_achievements(sender, instance, **kwargs):
    user_profile = instance.user
    # Check number of completed tennis sessions achievements
    check_achievement(user_profile,
                      "Tennis Sessions",
                      "Tennis Sessions",
                      [1, 5, 25, 50, 100])

    # Check category-specific achievements
    categories = ["backhand", "forehand", "serve", "volley",
                  "slice", "smash", "drop-shot", "agility", "stamina", "other"]

    for category in categories:
        check_achievement(user_profile,
                          "award_category_name",
                          f"Number of completed {category} lessons",
                          [5, 10, 25, 50, 100])

# Similar functions for other achievement checks (posts, likes, comments, follows, followers)
# ...


def check_achievement(user_profile, award_category_name, name, levels):
    """
    Check and award achievements for a specific task.
    """
    current_count = get_current_count(
        user_profile, award_category_name)  # Implement this function

    award_category = models.AchievementCategory.objects.get(
        name=award_category_name
    )

    for level, threshold in enumerate(levels, start=1):
        if current_count >= threshold:
            award_achievement(user_profile, award_category, name, level)


def get_current_count(user_profile, award_category):
    """
    Get the current count for a specific task.
    """
    # Implement logic to get the current count based on the task (e.g., completed sessions, posts, likes, comments, follows, followers)
    # ...

    if award_category == "Tennis Sessions":
        pass
    elif award_category == "Created Posts":
        pass
    elif award_category == "Liked Posts":
        pass
    elif award_category == "Comment Count":
        pass
    elif award_category == "Followed Count":
        pass
    elif award_category == "Followers Count":
        pass
    elif award_category == "Resources Read":
        pass
    elif award_category == "Backhand Sessions":
        pass
    elif award_category == "Forehand Sessions":
        pass
    elif award_category == "Serve Sessions":
        pass
    elif award_category == "Volley Sessions":
        pass
    elif award_category == "Slice Sessions":
        pass
    elif award_category == "Smash Sessions":
        pass
    elif award_category == "Drop-Shot Sessions":
        pass
    elif award_category == "Agility Sessions":
        pass
    elif award_category == "Stamina Sessions":
        pass


def award_achievement(user_profile, award_category, name, level):
    """
    Award an achievement to the user profile.
    """
    achievement = models.Achievement.objects.create(
        user_profile=user_profile,
        category=award_category,
        name=f"{name} Lvl {level}",
        description=f"Achieved Level {level} for {name}.",
        level=level
    )
    print(f"Achievement Awarded: {achievement}")
