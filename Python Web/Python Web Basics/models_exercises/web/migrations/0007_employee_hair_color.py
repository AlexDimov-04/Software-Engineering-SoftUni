# Generated by Django 4.2.1 on 2023-06-02 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_employee_years_of_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='hair_color',
            field=models.CharField(default='black', max_length=10),
            preserve_default=False,
        ),
    ]
