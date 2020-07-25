# Generated by Django 3.0.8 on 2020-07-19 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_profile_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='latitude',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='longitude',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
