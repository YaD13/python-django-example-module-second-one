# Generated by Django 2.1.2 on 2019-11-21 07:59

from django.db import migrations

from toolbox.constants import DATA_GOALS


def create_data_permissions(apps, schema_editor):
    data_permission = apps.get_model("toolbox", "DataPermission")

    data_permission.objects.update_or_create(
        code=DATA_GOALS,
        defaults=dict(
            name='Goal',
            endpoint='/goal/',
            method='GET',
            query_fields=[
                'user'
            ]
        )
    )

class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0016_create_portfolio_history_data_permissions'),
    ]

    operations = [
        migrations.RunPython(
            create_data_permissions, migrations.RunPython.noop
        )
    ]