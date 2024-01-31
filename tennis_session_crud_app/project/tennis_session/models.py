import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class TennisSession(models.Model):
    title = models.CharField(max_length=50)
    notes = models.TextField()
    date = models.DateTimeField()
    is_today = models.BooleanField()
    is_completed = models.BooleanField()

    def is_tennis_session_scheduled_today(self):
        today = timezone.now()

        if today.year == self.date.year:
            if today.month == self.date.month:
                if today.day == self.date.day:
                    return True
        return False
