# Generated by Django 3.0.3 on 2020-03-31 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carApp', '0005_auto_20200328_1925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
