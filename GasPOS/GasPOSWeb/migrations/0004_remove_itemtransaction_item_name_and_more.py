# Generated by Django 4.0.4 on 2022-05-25 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GasPOSWeb', '0003_dailytotal_in_charge_employee_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemtransaction',
            name='item_name',
        ),
        migrations.RemoveField(
            model_name='itemtransaction',
            name='item_price',
        ),
    ]