# Generated by Django 3.1.2 on 2021-04-28 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20210428_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='usercart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('pr_name', models.CharField(max_length=250)),
                ('pr_date', models.DateField()),
                ('pr_desc', models.CharField(max_length=500)),
                ('pr_price', models.IntegerField()),
                ('pr_img', models.ImageField(upload_to='shop/image')),
                ('Model', models.CharField(max_length=266)),
                ('color', models.CharField(default='Black', max_length=266)),
            ],
        ),
    ]
