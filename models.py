from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models

from toolbox.errors import ToolboxError, ERROR_NO_ENVIRONMENT_CONFIGURED


class DataPermission(models.Model):
    name = models.CharField(max_length=64)
    endpoint = models.CharField(max_length=128)
    method = models.CharField(max_length=6)
    code = models.CharField(max_length=64)
    query_fields = ArrayField(
        models.CharField(max_length=128),
        blank=True,
        null=True
    )
    body_fields = ArrayField(
        models.CharField(max_length=128),
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'tb_data_permission'

    def __str__(self):
        return self.name + ' permission'

    def get_query_fields(self):
        if self.query_fields:
            return self.query_fields
        else:
            return list()

    def get_body_fields(self):
        if self.body_fields:
            return self.body_fields
        else:
            return list()


class AccessGroup(models.Model):

    name = models.CharField(max_length=64)
    token = models.CharField(max_length=256)
    permissions = models.ManyToManyField(DataPermission)
    date_format_template = models.CharField(max_length=10, blank=True)

    class Meta:
        db_table = 'tb_access_group'

    def __str__(self):
        """
        Show string representation of AssetGroup
        """
        return self.name

    @staticmethod
    def get_base_url():
        """
        Retrieve Core.Route base URL set for current AccessGroup
        """
        if settings.CORE_ROUTE_URL:
            return settings.CORE_ROUTE_URL
        else:
            raise ToolboxError(
                ERROR_NO_ENVIRONMENT_CONFIGURED,
                'Core.Route URL is not set for environment'
            )
