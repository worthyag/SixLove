# Generated by Django 5.0.1 on 2024-03-09 18:19

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AchievementCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='achievement_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('level', models.PositiveIntegerField()),
                ('completed_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.userprofile')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.achievementcategory')),
            ],
        ),
    ]
