# Generated by Django 3.2.12 on 2023-07-14 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0002_auto_20230710_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customers',
        ),
    ]
