from django.core.management.base import BaseCommand
from models import UserProfile
from utils import check_achievement


class Command(BaseCommand):
    help = 'Award achievements for existing user activities.'

    def handle(self, *args, **options):
        # Iterate over all user profiles
        for user_profile in UserProfile.objects.all():
            # Awarding achievements for tennis sessions.
            check_achievement(user_profile.user, "Tennis Sessions",
                              "Tennis Sessions", [1, 5, 25, 50, 100])

            # Awarding achievement categories related to tennis sessions.
            categories = ["Backhand Sessions", "Forehand Sessions", "Serve Sessions",
                          "Volley Sessions", "Slice Sessions", "Smash Sessions",
                          "Drop-Shot Sessions", "Agility Sessions", "Stamina Sessions"]

            for category in categories:
                check_achievement(user_profile.user,
                                  category,
                                  category,
                                  [5, 10, 25, 50, 100])

            # Awarding achievements for number of created posts.
            check_achievement(user_profile.user,
                              "Created Posts",
                              "Created Posts",
                              [1, 5, 10, 15, 20, 25])

            # Awarding achievements for number of given likes.
            check_achievement(user_profile.user,
                              "Liked Posts",
                              "Liked Posts",
                              [5, 10, 25, 50, 100])

            # Awarding achievements for number of given comments.
            check_achievement(user_profile.user,
                              "Comment Count",
                              "Comment Count",
                              [1, 5, 10, 15, 20, 25])

            # Awarding achievements for number of users a user is following.
            check_achievement(user_profile.user,
                              "Followed Count",
                              "Followed Count",
                              [1, 2, 5, 10])

            # Awarding achievements for number of followers a user has.
            check_achievement(user_profile.user,
                              "Followers Count",
                              "Followers Count",
                              [1, 2, 5, 10])

            self.stdout.write(self.style.SUCCESS(
                f'Awarded achievements for user {user_profile.user.username}.'))
