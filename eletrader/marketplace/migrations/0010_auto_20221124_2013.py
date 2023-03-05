# Generated by Django 3.1 on 2022-11-24 20:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marketplace', '0009_order_clicks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='clicks',
        ),
        migrations.AddField(
            model_name='order',
            name='clicks',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]