
from django.db import migrations

from toolbox.constants import (
    DATA_ASSETS,
    DATA_NOTIFICATIONS,
    DATA_ASSET_CONTAINERS
)


def create_data_permissions(apps, schema_editor):
    data_permission = apps.get_model("toolbox", "DataPermission")

    data_permission.objects.all().delete()

    data_permission.objects.update_or_create(
        code=DATA_ASSETS,
        defaults=dict(
            name='Asset',
            endpoint='/asset/',
            method='GET',
            query_fields=[
                'type',
                'container',
                'group',
                'group_by',
                'sign',
                'portfolio',
                'collapse_prospery',
                'retrieve_service_a',
                'user'
            ]
        )
    )

    data_permission.objects.update_or_create(
        code=DATA_NOTIFICATIONS,
        defaults=dict(
            name='Notification',
            endpoint='/notifications/notifications/',
            method='GET',
            query_fields=[
                'type_id',
                'start_date',
                'end_date',
                'user'
            ]
        )
    )

    data_permission.objects.update_or_create(
        code=DATA_ASSET_CONTAINERS,
        defaults=dict(
            name='AssetContainer',
            endpoint='/asset-container/',
            method='GET',
            query_fields=[
                'source',
                'type',
                'group',
                'selected',
                'sign',
                'user'
            ]
        )
    )


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0005_auto_20190906_1154'),
    ]

    operations = [
        migrations.RunPython(
            create_data_permissions, migrations.RunPython.noop
        )
    ]
