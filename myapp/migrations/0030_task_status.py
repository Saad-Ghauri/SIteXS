# Generated by Django 4.2.6 on 2023-12-29 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
