# Generated by Django 3.2.7 on 2023-06-15 16:04

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_hansh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='picture',
            field=models.ImageField(blank=True, max_length=2500, null=True, upload_to=profiles.models.PathAndRename('picture/'), verbose_name='Зураг'),
        ),
    ]