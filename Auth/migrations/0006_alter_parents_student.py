# Generated by Django 5.0.2 on 2024-03-03 07:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0005_parents_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parents',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_student', to='Auth.students'),
        ),
    ]
