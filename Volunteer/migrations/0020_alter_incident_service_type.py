# Generated by Django 5.0.2 on 2024-11-22 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Volunteer', '0019_alter_incident_service_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='service_type',
            field=models.CharField(choices=[('Fire', 'Fire'), ('Police', 'Police'), ('Ambulance', 'Ambulance')], default='police', max_length=50),
        ),
    ]
