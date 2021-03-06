# Generated by Django 2.0.3 on 2018-04-01 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pk_stops', '0006_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot',
            name='booked_from',
        ),
        migrations.RemoveField(
            model_name='spot',
            name='booked_till',
        ),
        migrations.RemoveField(
            model_name='spot',
            name='is_booked',
        ),
        migrations.AddField(
            model_name='booking',
            name='booked_from',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='booked_till',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
