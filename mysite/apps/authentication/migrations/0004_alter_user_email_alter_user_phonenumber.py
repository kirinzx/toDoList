# Generated by Django 4.1.5 on 2023-06-06 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'This email has already been registered.'}, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phoneNumber',
            field=models.CharField(error_messages={'unique': 'This phone number has already been registered.'}, max_length=12, null=True, unique=True),
        ),
    ]
