# Generated by Django 3.2.7 on 2023-06-11 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_auto_20230607_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirm_password',
            field=models.CharField(max_length=7000),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=7000),
        ),
    ]
