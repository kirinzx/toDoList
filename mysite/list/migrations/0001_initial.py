# Generated by Django 4.1.5 on 2023-02-11 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.TextField()),
                ('password', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.TextField()),
            ],
        ),
    ]
