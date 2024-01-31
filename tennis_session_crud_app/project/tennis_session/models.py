import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class TennisSession(models.Model):
    title = models.CharField(max_length=150)
    notes = models.TextField()
    date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def is_tennis_session_scheduled_today(self):
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
