# Generated by Django 3.1.2 on 2021-04-26 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_contact_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
