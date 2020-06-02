from django.contrib import admin

from toolbox.models import AccessGroup, DataPermission


class AccessGroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'token', )

    @staticmethod
    def title(obj):
        return obj.__str__()


class DataPermissionAdmin(admin.ModelAdmin):
    readonly_fields = (
        'name',
        'method',
        'code',
        'query_fields',
        'body_fields'
    )

    list_display = ('__str__', 'endpoint', )

    ordering = ['name']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='',
                        extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        return super(DataPermissionAdmin, self).changeform_view(
            request, object_id, extra_context=extra_context
        )


admin.site.register(AccessGroup, AccessGroupAdmin)
admin.site.register(DataPermission, DataPermissionAdmin)
