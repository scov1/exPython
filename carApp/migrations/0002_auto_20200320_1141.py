# Generated by Django 3.0.3 on 2020-03-20 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='img',
            field=models.ImageField(blank=True, upload_to='img/', verbose_name='Изображение'),
        ),
    ]
