# Generated by Django 5.0.2 on 2024-03-04 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academics', '0007_course_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
    ]
