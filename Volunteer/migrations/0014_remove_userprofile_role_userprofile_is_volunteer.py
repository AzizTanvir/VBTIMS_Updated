# Generated by Django 5.0.2 on 2024-11-06 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0013_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='role',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_volunteer',
            field=models.BooleanField(default=True),
        ),
    ]
