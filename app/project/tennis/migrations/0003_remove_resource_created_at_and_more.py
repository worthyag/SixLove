# Generated by Django 5.0.1 on 2024-03-08 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tennis', '0002_remove_articlesection_article_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='created_by',
        ),
    ]
