# Generated by Django 4.1.5 on 2023-02-15 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_alter_user_password_alter_user_phonenumber_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password2',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]