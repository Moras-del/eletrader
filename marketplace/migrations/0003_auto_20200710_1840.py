# Generated by Django 3.0.8 on 2020-07-10 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_auto_20200710_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='type',
            field=models.CharField(choices=[('Sprzedaż', 'Sprzedaż'), ('Kupno', 'Kupno')], max_length=20),
        ),
    ]
