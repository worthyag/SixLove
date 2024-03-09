from django.db.models import Count

from tennis import models as TennisModels

from . import models


def check_achievement(user, award_category_name, name, levels):
    """
    Checks and awards achievements for a specific task.
    """
    current_count = get_current_count(user, award_category_name)

    award_category = models.AchievementCategory.objects.get(
        name=award_category_name
    )

    # Getting the user profile of the user.
    user_profile = models.UserProfile.objects.get(user=user)

    for level, threshold in enumerate(levels, start=1):
        # Checking if the user has already received the achievement.
        if not has_achievement(user_profile, award_category, level):
            if current_count >= threshold:
                award_achievement(user_profile, award_category, name, level)


def has_achievement(user_profile, award_category, level):
    """
    Checks if the user has already received the achievement for
    a specific category and level.
    """
    return models.Achievement.objects.filter(
        user_profile=user_profile,
        category=award_category,
        level=level
    ).exists()


def get_current_count(user, award_category):
    """
    Returns the current count for a specific task (award category).
    """
    # Getting the user profile of the user.
    user_profile = models.UserProfile.objects.get(user=user)

    if award_category == "Tennis Sessions":
        tennis_sessions = TennisModels.TennisSession.objects.filter(
            user=user,
            is_completed=True
        )

        # Getting the count of the tennis sessions.
        return tennis_sessions.count()

    elif award_category == "Created Posts":
        # Getting the count of the users posts.
        return user_profile.user_posts.count()

    elif award_category == "Liked Posts":
        # Getting the count of the user's given likes.
        return user_profile.like_set.count()

    elif award_category == "Comment Count":
        # Getting the count of the user's given comments.
        return user_profile.comment_set.count()

    elif award_category == "Followed Count":
        # Getting the count of the user's followed users.
        return user_profile.following.count()

    elif award_category == "Followers Count":
        # Getting the count of the user's followers.
        return user_profile.followers.count()

    elif award_category == "Resources Read":
        pass

    elif award_category == "Backhand Sessions":
        backhand_sessions = TennisModels.TennisSession.objects.filter(
            user=user,
            category="backhand",
            is_completed=True
        )

        # Getting the count of the backhand tennis sessions.
        return backhand_sessions.count()

    elif award_category == "Forehand Sessions":
        forehand_sessions = TennisModels.TennisSession.objects.filter(
            user=user,
            category="forehand",
            is_completed=True
        )

        # Getting the count of the forehand tennis sessions.
        return forehand_sessions.count()

    elif award_category == "Serve Sessions":
        serve_sessions = TennisModels.TennisSession.objects.filter(
            user=user,
            category="serve",
            is_completed=True
        )

        # Getting the count of the serve tennis sessions.
        return serve_sessions.count()

    elif award_category == "Volley Sessions":
        volley_sessions = TennisModels.TennisSession.objects.filter(
            user=user,
            category="volley",
            is_completed=True
        )

        # Getting the count of the volley tennis sessions.
        return volley_sessions.count()

    elif award_category == "Slice Sessions":
        slice_sessions = TennisModels.TennisSession.objects.filter(
            user=user,
            category="slice",
            is_completed=True
        )

        # Getting the count of the slice tennis sessions.
        return slice_sessions.count()

    elif award_category == "Smash Sessions":
        smash_sessions = TennisModels.TennisSession.objects.filter(
            user=user,
            category="smash",
            is_completed=True
        )

        # Getting the count of the smash tennis sessions.
        return smash_sessions.count()

    elif award_category == "Drop-Shot Sessions":
        drop_shot_sessions = TennisModels.TennisSession.objects.filter(
            user=user,
            category="drop-shot",
            is_completed=True
        )

        # Getting the count of the drop-shot tennis sessions.
        return drop_shot_sessions.count()

    elif award_category == "Agility Sessions":
        agility_sessions = TennisModels.TennisSession.objects.filter(
            user=user,
            category="agility",
            is_completed=True
        )

        # Getting the count of the agility tennis sessions.
        return agility_sessions.count()

    elif award_category == "Stamina Sessions":
        stamina_sessions = TennisModels.TennisSession.objects.filter(
            user=user,
            category="stamina",
            is_completed=True
        )

        # Getting the count of the stamina tennis sessions.
        return stamina_sessions.count()


def award_achievement(user_profile, award_category, name, level):
    """
    Awards an achievement to the user profile.
    """
    achievement = models.Achievement.objects.create(
        user_profile=user_profile,
        category=award_category,
        name=f"{name} Lvl {level}",
        description=f"Achieved Level {level} for {name}.",
        level=level
    )
    print(f"Achievement Awarded: {achievement}")
