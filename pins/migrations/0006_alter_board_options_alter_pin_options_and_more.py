# Generated by Django 5.0.2 on 2024-03-04 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pins', '0005_alter_pin_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'verbose_name_plural': 'Панель постов'},
        ),
        migrations.AlterModelOptions(
            name='pin',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterModelOptions(
            name='pinner',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
