# Generated by Django 4.2.2 on 2023-06-11 18:51

import django.core.validators
from django.db import migrations, models
import exam_prep_3.web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Sports Car', 'Sports Car'), ('Pickup', 'Pickup'), ('Crossover', 'Crossover'), ('Minibus', 'Minibus'), ('Other', 'Other')], max_length=10)),
                ('model', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)])),
                ('year', models.IntegerField(validators=[exam_prep_3.web.models.year_validation])),
                ('image_url', models.URLField()),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0)])),
            ],
        ),
    ]
