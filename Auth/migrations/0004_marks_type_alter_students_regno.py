# Generated by Django 5.0.2 on 2024-03-02 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0003_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='type',
            field=models.CharField(choices=[('Test', 'test'), ('Exam', 'exam'), ('Assignment', 'Assignment')], default='Assignment', max_length=255),
        ),
        migrations.AlterField(
            model_name='students',
            name='regNo',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
