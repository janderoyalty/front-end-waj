# Generated by Django 4.0.6 on 2022-07-28 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_four',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_num',
            field=models.IntegerField(),
        ),
    ]
