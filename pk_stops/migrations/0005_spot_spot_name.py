# Generated by Django 2.0.3 on 2018-03-31 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pk_stops', '0004_auto_20180331_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='spot',
            name='spot_name',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]