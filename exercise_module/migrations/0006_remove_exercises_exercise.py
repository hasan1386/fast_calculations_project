# Generated by Django 4.1.5 on 2023-03-27 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_module', '0005_alter_exercises_exercise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercises',
            name='exercise',
        ),
    ]