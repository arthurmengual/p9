# Generated by Django 3.2.9 on 2021-12-04 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flux', '0003_rename_headline_review_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='body',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='rating',
            new_name='note',
        ),
    ]