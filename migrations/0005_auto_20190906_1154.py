# Generated by Django 2.1.2 on 2019-09-06 11:54

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0003_create_data_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='datapermission',
            name='body_fields',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='datapermission',
            name='query_fields',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), blank=True, null=True, size=None),
        ),
    ]