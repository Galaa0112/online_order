# Generated by Django 3.2.7 on 2023-06-07 08:23

from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_auto_20230607_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Гарчиг')),
            ],
            options={
                'verbose_name': 'Тусламж',
                'verbose_name_plural': 'Тусламж',
                'db_table': 'help',
            },
        ),
        migrations.CreateModel(
            name='HelpContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, default='', null=True, verbose_name='Текст')),
                ('picture', models.ImageField(blank=True, max_length=2500, upload_to=profiles.models.PathAndRename('picture/'), verbose_name='Зураг')),
            ],
            options={
                'verbose_name': 'Контент',
                'verbose_name_plural': 'Контент',
                'db_table': 'help_content',
            },
        ),
        migrations.CreateModel(
            name='HelpStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Гарчиг')),
                ('contents', models.ManyToManyField(to='profiles.HelpContent')),
                ('help', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='help_step', to='profiles.help', verbose_name='Тусламж')),
            ],
            options={
                'verbose_name': 'Алхам',
                'verbose_name_plural': 'Алхам',
                'db_table': 'help_step',
            },
        ),
    ]
