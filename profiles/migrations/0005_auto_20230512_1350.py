# Generated by Django 3.2.7 on 2023-05-12 05:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_from_application',
        ),
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Бүртгэгдсэн'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Засагдсан'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Хаяг'),
        ),
    ]
