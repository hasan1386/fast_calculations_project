# Generated by Django 4.1.5 on 2023-03-27 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_module', '0008_remove_exercises_title_alter_exercises_exercise'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercises',
            old_name='exercise',
            new_name='lesson',
        ),
    ]
