# Generated by Django 4.2.6 on 2023-10-31 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_image_description_image_date_image_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
