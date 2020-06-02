from django.urls import re_path

from toolbox.api_views import (
    AccessGroupsAPIView,
    AccessGroupAPIView
)

app_name = 'toolbox'

urlpatterns = [
    re_path(r'^access_groups/$',
            AccessGroupsAPIView.as_view(),
            name='access_groups_list'),
    re_path(r'^access_group/(?P<access_group_id>\d+)/$',
            AccessGroupAPIView.as_view(),
            name='access_group'),
]
