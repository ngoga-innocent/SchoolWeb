# Generated by Django 5.0.2 on 2024-03-03 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academics', '0004_internships_registeredinterns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internships',
            name='starting',
            field=models.DateField(),
        ),
    ]
