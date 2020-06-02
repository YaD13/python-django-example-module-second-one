

from django.db import migrations

from toolbox.constants import DATA_ORDERS, DATA_RECURRENT_ORDERS


def create_data_permissions(apps, schema_editor):
    data_permission = apps.get_model("toolbox", "DataPermission")

    data_permission.objects.update_or_create(
        code=DATA_ORDERS,
        defaults=dict(
            name='Order',
            endpoint='/asset-container/orders',
            method='GET',
            query_fields=[
                'quantity',
                'container_id',
                'user'
            ]
        )
    )

    data_permission.objects.update_or_create(
        code=DATA_RECURRENT_ORDERS,
        defaults=dict(
            name='Recurrent order',
            endpoint='/asset/recurrent_orders',
            method='GET',
            query_fields=[
                'user'
            ]
        )
    )



class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0007_accessgroup_environment_setting'),
    ]

    operations = [
        migrations.RunPython(
            create_data_permissions, migrations.RunPython.noop
        )
    ]
