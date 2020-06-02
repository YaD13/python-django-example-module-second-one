# Generated by Django 2.1.2 on 2019-11-05 11:56

from django.db import migrations

from toolbox.constants import DATA_PORTFOLIO_PERFORMANCE


def create_data_permissions(apps, schema_editor):
    data_permission = apps.get_model("toolbox", "DataPermission")

    data_permission.objects.update_or_create(
        code=DATA_PORTFOLIO_PERFORMANCE,
        defaults=dict(
            name='Portfolio performance',
            endpoint='/asset/simple-performance/',
            method='GET',
            query_fields=[
                'start_date',
                'end_date',
                'user',
            ]
        )
    )

class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0014_create_internal_reports_data_permissions'),
    ]

    operations = [
        migrations.RunPython(
            create_data_permissions, migrations.RunPython.noop
        )
    ]
