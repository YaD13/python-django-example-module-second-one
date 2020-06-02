# Generated by Django 2.1.2 on 2019-11-22 14:40

from django.db import migrations

from toolbox.constants import DATA_FREQUENCY_TYPES

def create_data_permissions(apps, schema_editor):
    data_permission = apps.get_model("toolbox", "DataPermission")

    data_permission.objects.update_or_create(
        code=DATA_FREQUENCY_TYPES,
        defaults=dict(
            name='Frequency types',
            endpoint='/goal/frequency_types/',
            method='GET',
            query_fields=[]
        )
    )


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0018_change_recurent_orders_data_permissions'),
    ]

    operations = [
        migrations.RunPython(
            create_data_permissions, migrations.RunPython.noop
        )
    ]
