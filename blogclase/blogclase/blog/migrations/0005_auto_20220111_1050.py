# Generated by Django 3.2.11 on 2022-01-11 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(verbose_name='Fecha Post'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='intro',
            field=models.CharField(max_length=250, verbose_name='Introducción'),
        ),
    ]
