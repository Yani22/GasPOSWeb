# Generated by Django 4.0.4 on 2022-05-25 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GasPOSWeb', '0005_remove_gastransaction_gas_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeelogin',
            old_name='password',
            new_name='date_logged_out',
        ),
        migrations.RemoveField(
            model_name='employeelogin',
            name='random_digit',
        ),
        migrations.RemoveField(
            model_name='employeelogin',
            name='username',
        ),
    ]