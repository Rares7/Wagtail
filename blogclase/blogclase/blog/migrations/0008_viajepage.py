# Generated by Django 4.0.3 on 2022-03-07 18:53

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('blog', '0007_alter_blogpagetag_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViajePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('info', wagtail.core.fields.RichTextField(blank=True)),
                ('coordenadas', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
