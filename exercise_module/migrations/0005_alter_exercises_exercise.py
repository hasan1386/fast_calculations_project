# Generated by Django 4.1.5 on 2023-03-27 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons_module', '0002_alter_lessons_options'),
        ('exercise_module', '0004_remove_exercises_exercise_exercises_exercise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercises',
            name='exercise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='lessons_module.lessons', verbose_name='درس مربوطه'),
        ),
    ]
