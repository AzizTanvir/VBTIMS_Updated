# Generated by Django 5.0.2 on 2024-11-06 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0014_remove_userprofile_role_userprofile_is_volunteer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_volunteer',
            field=models.BooleanField(default=False),
        ),
    ]
