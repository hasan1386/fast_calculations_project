# Generated by Django 4.1.5 on 2023-03-29 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0002_footerlinktitle_alter_sitesettings_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footerlinkitems',
            name='category',
        ),
        migrations.DeleteModel(
            name='FooterLinkTitle',
        ),
    ]
