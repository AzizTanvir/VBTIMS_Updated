# Generated by Django 5.0.2 on 2024-11-12 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0015_alter_userprofile_is_volunteer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_picture',
        ),
    ]
