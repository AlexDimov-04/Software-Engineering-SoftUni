# Generated by Django 4.2.2 on 2023-06-11 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image_url',
            field=models.URLField(verbose_name='Image URL'),
        ),
    ]