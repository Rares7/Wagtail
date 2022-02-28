# Generated by Django 3.2.11 on 2022-01-26 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0002_pelicula'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pelicula',
            old_name='image',
            new_name='imagen',
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='title',
            field=models.CharField(max_length=250, verbose_name='título'),
        ),
    ]
