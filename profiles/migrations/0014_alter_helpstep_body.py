# Generated by Django 3.2.7 on 2023-06-07 08:59

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_auto_20230607_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helpstep',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Контент'),
        ),
    ]
