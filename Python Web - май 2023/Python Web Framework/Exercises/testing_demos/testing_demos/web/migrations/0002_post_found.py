# Generated by Django 4.2.2 on 2023-07-12 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='found',
            field=models.BooleanField(default=False),
        ),
    ]
