# Generated by Django 3.2.7 on 2023-05-16 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20230513_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Устгасан'),
        ),
    ]
