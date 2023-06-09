# Generated by Django 4.2.1 on 2023-06-02 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_employee_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('code_name', models.CharField(max_length=10, unique=True)),
                ('deadline', models.DateField()),
            ],
        ),
    ]