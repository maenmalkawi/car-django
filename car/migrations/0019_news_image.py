# Generated by Django 4.2.16 on 2025-02-16 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0018_car_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
