# Generated by Django 4.1.5 on 2023-02-16 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_user_password2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password2',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phoneNumber',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]