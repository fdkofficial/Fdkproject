# Generated by Django 3.1.2 on 2021-04-27 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210427_1804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moreimages',
            old_name='Images',
            new_name='images',
        ),
    ]
