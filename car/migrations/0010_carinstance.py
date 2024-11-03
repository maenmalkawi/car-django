# Generated by Django 5.1.1 on 2024-10-30 00:08

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0009_alter_typecar_cartype'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarInstance',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, help_text='Unique id for this car', primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, choices=[('A', 'AVAILABLE'), ('U', 'UNAVAILABLE')], default='A', help_text='Car availability status', max_length=2)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='car_instance', to='car.car')),
            ],
            options={
                'ordering': ['Id'],
            },
        ),
    ]