# Generated by Django 4.2.6 on 2023-12-06 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_remove_hotspot_image_hotspot_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotspot',
            name='image',
        ),
        migrations.AddField(
            model_name='hotspot',
            name='images',
            field=models.ManyToManyField(to='myapp.imagemodel'),
        ),
    ]