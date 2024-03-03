from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.


class UserProfile(models.Model):
    """"""
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        default='./community/images/profile-pic-temp.png'
    )
    bio = models.TextField(blank=True)
    username = models.CharField(max_length=50)
    profile_name = models.CharField(max_length=50)

    # Represents the many-to-many relationships between users for followers and following.
    # Allows me to retrieve the set of users who are followers and whom a user is following.
    followers = models.ManyToManyField(
        'self', symmetrical=False, related_name='followers_set', blank=True)
    following = models.ManyToManyField(
        'self', symmetrical=False, related_name='following_set', blank=True)

    def __str__(self):
        return self.username

    def follow(self, user_to_follow):
        """"""
        self.following.add(user_to_follow)
        user_to_follow.followers.add(self)

    def unfollow(self, user_to_unfollow):
        """"""
        self.following.remove(user_to_unfollow)
        user_to_unfollow.followers.remove(self)

    def toggle_follow(self, other_user_profile):
        """"""
        if self.following.filter(id=other_user_profile.id).exists():
            self.unfollow(other_user_profile)
            return False
        else:
            self.follow(other_user_profile)
            return True

    # Dynamically get the follower count.
    def get_followers_count(self):
        """"""
        return self.followers.count()

    # Dynamically get the following count.
    def get_following_count(self):
        """"""
        return self.following.count()


class Follow(models.Model):
    """"""
    follower = models.ForeignKey(
        UserProfile, related_name="followed_by", on_delete=models.CASCADE)
    followed = models.ForeignKey(
        UserProfile, related_name="following_user", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.follower} follows {self.followed}'


class UserPosts(models.Model):
    """"""
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='user_posts')
    post_picture = models.ImageField(
        upload_to='post_pics/'
    )
    post_caption = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(
        UserProfile,
        related_name='post_likes',
        through='Like')
    comments = models.ManyToManyField(
        UserProfile,
        related_name='post_comments',
        through='Comment')

    def __str__(self):
        return f"{self.user_profile.username}'s post - {self.created_at}"

    def delete(self, *args, **kwargs):
        """"""
        # Deleting the associated picture when the post is deleted.
        try:
            storage, path = self.post_picture.storage, self.post_picture.path
            super(UserPosts, self).delete(*args, **kwargs)
            storage.delete(path)
        except FileNotFoundError:
            print("File does not exist.")

    # def like(self, user_profile):
    #     """"""
    #     like_instance, created = Like.objects.get_or_create(
    #         user_profile=user_profile,
    #         post=self
    #     )

    #     if created:
    #         self.likes.add(user_profile)

    # def remove_like(self, user_profile):
    #     """"""
    #     like_instance = Like.objects.filter(
    #         user_profile=user_profile, post=self
    #     ).first()

    #     if like_instance:
    #         like_instance.delete()
    #         self.likes.remove(user_profile)

    def toggle_like(self, user_profile):
        """Toggle like on the post."""
        like_instance, created = Like.objects.get_or_create(
            user_profile=user_profile,
            post=self
        )

        if created:
            self.likes.add(user_profile)
            liked = True
        else:
            like_instance.delete()
            self.likes.remove(user_profile)
            liked = False

        return liked

    def comment(self, user_profile, text):
        """"""
        comment_instance = Comment.objects.create(
            user_profile=user_profile,
            post=self,
            text=text
        )

        self.comments.add(comment_instance)

    def remove_comment(self, comment_instance):
        """"""
        if comment_instance in self.comments.all():
            comment_instance.delete()
            self.comments.remove(comment_instance)

    def get_like_count(self):
        """"""
        return self.likes.count()

    def get_comment_count(self):
        """"""
        return self.comments.count()


class Like(models.Model):
    """"""
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(UserPosts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user_profile.username} likes {self.post.user_profile.username}'s post"


class Comment(models.Model):
    """"""
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(UserPosts, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user_profile.username}'s comment on {self.post.user_profile.username}'s post"
