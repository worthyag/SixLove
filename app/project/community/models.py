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


class Follow(models.Model):
    """"""
    follower = models.ForeignKey(
        UserProfile, related_name="following", on_delete=models.CASCADE)
    followed = models.ForeignKey(
        UserProfile, related_name="followers", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.follower} follows {self.followed}'


class UserPosts(models.Model):
    """"""
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post_picture = models.ImageField(
        upload_to='post_pics/'
    )
    post_caption = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    likes = models.ManyToManyField(
        UserProfile,
        related_name='post_likes',
        through=Like)
    comments = models.ManyToManyField(
        UserProfile,
        related_name='post_comments',
        through=Comment)

    def __str__(self):
        return f"{self.user_profile.username}'s post - {self.created_at}"

    def like(self, user_profile):
        """"""
        Like.objects.create(user_profile=user_profile, post=self)
        self.likes.add(user_profile)

    def remove_like(self, user_profile):
        """"""
        like_instance = Like.objects.filter(
            user=user_profile, post=self).first()
        if like_instance:
            like_instance.delete()
            self.likes.remove(user_profile)

    def comment(self, user_profile, text):
        """"""
        Comment.objects.create(user_profile=user_profile, post=self, text=text)
        self.comments.add(user_profile)

    def remove_comment(self, user_profile, text):
        """"""
        comment_instance = Comment.objects.filter(
            user=user_profile,
            post=self,
            text=text
        ).first()

        if comment_instance:
            comment_instance.delete()
            self.comments.remove(user_profile)


class Like(models.Model):
    """"""
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(UserPosts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.user_profile.username} likes {self.post.user_profile.username}'s post"


class Comment(models.Model):
    """"""
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(UserPosts, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.user_profile.username}'s comment on {self.post.user_profile.username}'s post"
