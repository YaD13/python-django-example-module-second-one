# Generated by Django 2.1.2 on 2019-09-17 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0008_create_order_and_recurrent_order_data_permissions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessgroup',
            name='environment_setting',
        ),
    ]