# Generated by Django 3.0 on 2021-05-13 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_logindata'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_historie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id1', models.CharField(max_length=255)),
            ],
        ),
    ]
