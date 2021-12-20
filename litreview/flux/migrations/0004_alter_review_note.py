# Generated by Django 4.0 on 2021-12-20 18:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flux', '0003_alter_review_titler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='note',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
