# Generated by Django 4.0.6 on 2022-07-28 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='delete',
            field=models.BooleanField(default=False),
        ),
    ]
