# Generated by Django 2.1.2 on 2019-09-10 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0006_create_new_data_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessgroup',
            name='environment_setting',
            field=models.CharField(choices=[('dev', 'Development'), ('test', 'Test'), ('acp', 'Acceptance'), ('prod', 'Production')], default='dev', max_length=4),
        ),
    ]
