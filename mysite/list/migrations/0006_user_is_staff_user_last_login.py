# Generated by Django 4.1.5 on 2023-02-17 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0005_remove_user_password2_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]