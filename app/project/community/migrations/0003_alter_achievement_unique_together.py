# Generated by Django 5.0.1 on 2024-03-09 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_achievementcategory_achievement'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='achievement',
            unique_together={('user_profile', 'category', 'level')},
        ),
    ]
