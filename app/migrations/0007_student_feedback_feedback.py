# Generated by Django 4.1.5 on 2023-04-12 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_student_feedback_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_feedback',
            name='feedback',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
