# Generated by Django 4.2.1 on 2023-06-02 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0021_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='project',
            field=models.ManyToManyField(to='web.project'),
        ),
    ]
