# Generated by Django 3.1.2 on 2021-04-27 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='idr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
