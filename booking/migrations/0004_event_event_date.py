# Generated by Django 3.2.20 on 2023-07-20 16:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_remove_booking_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(default=django.utils.timezone.localtime),
        ),
    ]