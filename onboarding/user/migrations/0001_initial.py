# Generated by Django 4.2.4 on 2023-08-14 10:40

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
                ('user_email', models.CharField(max_length=32, unique=True)),
                ('user_password', models.CharField(max_length=128)),
            ],
        ),
    ]
