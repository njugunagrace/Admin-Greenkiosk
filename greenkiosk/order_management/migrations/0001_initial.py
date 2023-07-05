# Generated by Django 4.2.1 on 2023-06-30 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customers', models.CharField(max_length=32)),
                ('date', models.DateField()),
                ('products', models.CharField(max_length=32)),
                ('delivery_options', models.CharField(max_length=32)),
                ('delivery_date', models.DateTimeField()),
            ],
        ),
    ]
