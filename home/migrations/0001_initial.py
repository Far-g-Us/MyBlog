# Generated by Django 4.2.5 on 2023-09-21 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='home/image/', verbose_name='Изображение')),
                ('date', models.DateField(verbose_name='Дата')),
                ('url', models.URLField(blank=True, verbose_name='Доп. источник')),
            ],
        ),
    ]