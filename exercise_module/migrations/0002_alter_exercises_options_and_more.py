# Generated by Django 4.1.5 on 2023-03-27 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercises',
            options={'verbose_name': 'تمرین', 'verbose_name_plural': 'تمرینات'},
        ),
        migrations.RemoveField(
            model_name='exercises',
            name='operator_type',
        ),
    ]