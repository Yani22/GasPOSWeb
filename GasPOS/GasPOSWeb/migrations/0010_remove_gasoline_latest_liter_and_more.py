# Generated by Django 4.0.4 on 2022-05-26 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GasPOSWeb', '0009_remove_employee_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gasoline',
            name='latest_liter',
        ),
        migrations.RemoveField(
            model_name='gasoline',
            name='previous_liter',
        ),
        migrations.RemoveField(
            model_name='gasoline',
            name='total_liter',
        ),
    ]
