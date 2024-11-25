# Generated by Django 4.1.5 on 2023-04-04 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_student_feedback_emotion'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_feedback',
            name='standard',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student_feedback',
            name='student_roll_no',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student_feedback',
            name='student_name',
            field=models.CharField(max_length=70),
        ),
    ]
