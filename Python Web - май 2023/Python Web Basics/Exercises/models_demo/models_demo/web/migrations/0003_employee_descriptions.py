# Generated by Django 4.2.1 on 2023-05-31 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_employee_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='descriptions',
            field=models.TextField(default='na dqdo mi taratancite'),
            preserve_default=False,
        ),
    ]
