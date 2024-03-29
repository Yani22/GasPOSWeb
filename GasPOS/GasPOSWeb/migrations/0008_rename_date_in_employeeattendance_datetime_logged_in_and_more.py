# Generated by Django 4.0.4 on 2022-05-25 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GasPOSWeb', '0007_remove_employeelogin_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeattendance',
            old_name='date_in',
            new_name='datetime_logged_in',
        ),
        migrations.RenameField(
            model_name='employeeattendance',
            old_name='date_out',
            new_name='datetime_logged_out',
        ),
        migrations.RemoveField(
            model_name='employeeattendance',
            name='employee_name',
        ),
        migrations.RemoveField(
            model_name='employeeattendance',
            name='time_in',
        ),
        migrations.RemoveField(
            model_name='employeeattendance',
            name='time_out',
        ),
    ]
