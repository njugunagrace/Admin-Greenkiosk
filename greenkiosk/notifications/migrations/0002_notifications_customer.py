# Generated by Django 3.2.12 on 2023-07-10 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_user'),
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='customer',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
            preserve_default=False,
        ),
    ]
