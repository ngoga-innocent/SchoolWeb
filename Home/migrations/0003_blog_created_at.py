# Generated by Django 5.0.2 on 2024-03-05 07:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]