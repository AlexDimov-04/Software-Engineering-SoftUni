# Generated by Django 4.2.1 on 2023-06-02 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.department'),
            preserve_default=False,
        ),
    ]
