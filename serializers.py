from rest_framework import serializers

from accounts.models import UserProfile
from toolbox.models import AccessGroup, DataPermission


class DataPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPermission
        fields = ('id', 'name', 'code', )


class AccessGroupSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    @staticmethod
    def get_permissions(instance):
        codes = []
        for item in instance.permissions.get_queryset():
            codes.append(item.code)
        return codes

    @staticmethod
    def get_name(instance):
        return instance.__str__()

    class Meta:
        model = AccessGroup
        fields = ('id', 'name', 'permissions', 'date_format_template', )


class UserProfileSerializer(serializers.ModelSerializer):
    access_groups = AccessGroupSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ('user', 'default_group', 'active_group', 'access_groups', )
