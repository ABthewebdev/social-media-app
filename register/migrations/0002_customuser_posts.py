# Generated by Django 5.1.6 on 2025-03-05 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='posts',
            field=models.BigIntegerField(default=0),
        ),
    ]
