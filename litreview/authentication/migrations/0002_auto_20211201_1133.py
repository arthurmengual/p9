# Generated by Django 3.2.9 on 2021-12-01 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_photo',
        ),
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]
