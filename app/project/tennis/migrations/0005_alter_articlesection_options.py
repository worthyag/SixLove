# Generated by Django 5.0.1 on 2024-03-08 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tennis', '0004_tag_alter_resource_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlesection',
            options={'ordering': ['resource', 'id']},
        ),
    ]
