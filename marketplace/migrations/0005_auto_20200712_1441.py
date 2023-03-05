# Generated by Django 3.0.8 on 2020-07-12 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0004_auto_20200712_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='item_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.DecimalField(decimal_places=0, max_digits=5),
        ),
    ]
