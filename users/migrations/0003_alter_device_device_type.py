# Generated by Django 5.2 on 2025-04-16 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_device_device_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'WEB'), (3, 'ANDROID'), (2, 'IOS')], default=1),
        ),
    ]
