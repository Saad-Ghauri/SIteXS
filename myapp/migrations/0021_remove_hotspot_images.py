# Generated by Django 4.2.6 on 2023-12-07 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_delete_hotspotimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotspot',
            name='images',
        ),
    ]