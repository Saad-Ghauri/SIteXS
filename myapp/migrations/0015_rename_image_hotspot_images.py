# Generated by Django 4.2.6 on 2023-12-06 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_rename_images_hotspot_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotspot',
            old_name='image',
            new_name='images',
        ),
    ]
