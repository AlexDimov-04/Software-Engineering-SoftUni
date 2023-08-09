# Generated by Django 4.2.2 on 2023-08-09 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('username', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, related_name='app_users', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='app_users', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
