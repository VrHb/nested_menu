# Generated by Django 4.1.7 on 2023-03-24 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название меню')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, verbose_name='Часть меню для url')),
                ('url', models.CharField(blank=True, max_length=250, null=True, verbose_name='Имя url')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название элемента')),
                ('url', models.CharField(blank=True, max_length=250, verbose_name='Ссылка')),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='menu_app.menu')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='menu_app.menuitem')),
            ],
            options={
                'verbose_name': 'Элемент меню',
                'verbose_name_plural': 'Элементы меню',
            },
        ),
    ]
