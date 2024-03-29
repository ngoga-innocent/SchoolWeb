# Generated by Django 5.0.2 on 2024-03-01 19:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academics', '0001_initial'),
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='id',
        ),
        migrations.AddField(
            model_name='students',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Academics.course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='students',
            name='regNo',
            field=models.TextField(default='1', max_length=255, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
