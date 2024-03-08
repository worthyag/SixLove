import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.


class TennisSession(models.Model):
    """"""
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    notes = models.TextField()
    date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def is_tennis_session_scheduled_today(self):
        """"""
        today = timezone.now()

        if type(self.date) != type(""):
            if today.year == self.date.year:
                if today.month == self.date.month:
                    if today.day == self.date.day:
                        return True
            return False
        else:
            if today.year == int(self.date[:4]):
                if today.month == int(self.date[5:7]):
                    if today.day == int(self.date[8:11]):
                        return True
            return False

    def __str__(self):
        """"""
        return f"{self.user.get_username()} - {self.title}"


class Tag(models.Model):
    """"""
    RESOURCE_TAGS = [
        ("backhand", "Backhand"),
        ("forehand", "Forehand"),
        ("warm_up", "Warm Up"),
        ("cool_down", "Cool Down"),
        ("stretching", "Stretching"),
        ("serve", "Serve"),
        ("agility", "Agility"),
        ("volley", "Volley"),
        ("slice", "Slice"),
        ("stamina", "Stamina"),
        ("tnlp", "TNLP"),
        ("other", "Other")
    ]

    name = models.CharField(max_length=255, unique=True, choices=RESOURCE_TAGS)

    def __str__(self):
        return self.name


class Resource(models.Model):
    """"""
    RESOURCE_TYPES = [
        ("video", "Video"),
        ("article", "Article")
    ]

    title = models.CharField(max_length=255)
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    tags = models.ManyToManyField(Tag, blank=True)
    reference = models.URLField()
    # video_url = models.URLField(blank=True, null=True)
    video_url = models.CharField(max_length=20, blank=True, null=True)
    article_image = models.ImageField(upload_to="article_images/",
                                      blank=True, null=True)

    # created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # Many-to-Many relationship with ArticleSection
    sections = models.ManyToManyField(
        "ArticleSection", blank=True, related_name="resources")

    def __str__(self):
        """"""
        return f"{self.title}"


class ArticleSection(models.Model):
    """"""
    SECTION_TYPES = [
        ("heading", "Heading"),
        ("paragraph", "Paragraph"),
        ("image", "Image"),
        ("bullet_points", "Bullet Points")
    ]

    # article = models.ForeignKey(Resource, on_delete=models.CASCADE,
    # related_name="article_sections",
    # blank=True, null=True)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE,
                                 related_name="article_sections",
                                 default=None)
    section_type = models.CharField(max_length=15, choices=SECTION_TYPES)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="article_images/",
                              blank=True, null=True)

    class Meta:
        ordering = ['resource', 'id']

    def __str__(self):
        """"""
        return f"{self.section_type} - {self.resource.title} - \
            {self.content[:20] if self.content else 'No Content'}"
