# Generated by Django 3.2 on 2022-05-16 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={'verbose_name_plural': 'Ratings'},
        ),
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'verbose_name_plural': 'Stars of rating'},
        ),
    ]
