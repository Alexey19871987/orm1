# Generated by Django 4.0.4 on 2022-07-05 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.URLField(max_length=255, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название телефона'),
        ),
    ]
