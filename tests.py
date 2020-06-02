from django.urls import reverse
from rest_framework import status

from toolbox.errors import ToolboxError, TEST_ERROR
from toolbox.models import AccessGroup
from utils_testing.testing_tools import BasicTestCase


class GroupsTestCase(BasicTestCase):

    def send_request(self, user_profile, user_data):
        url = reverse('api_v1:toolbox_api:access_groups_list')

        data = dict(
            user_id=user_profile.user.id,
        )

        user_profile.get_full_name()

        headers = dict(
            HTTP_AUTHORIZATION='Bearer ' + user_data['token']
        )

        return self.client.get(url, data, **headers)

    def test_get_groups(self):
        user_data = self.log_in(self.user_profile)
        response = self.send_request(self.user_profile, user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @staticmethod
    def test_error():
        error = ToolboxError(TEST_ERROR)
        error.get_data()


class GroupTestCase(BasicTestCase):

    def send_request(self, user_profile, user_data):
        access_group = AccessGroup.objects.first()

        url = reverse('api_v1:toolbox_api:access_group', args=[access_group.id, ])

        data = dict(
            user_id=user_profile.user.id,
        )

        user_profile.get_full_name()

        headers = dict(
            HTTP_AUTHORIZATION='Bearer ' + user_data['token']
        )

        return self.client.put(url, data, "application/json", **headers)

    def test_change_active_group(self):
        user_data = self.log_in(self.user_profile)
        response = self.send_request(self.user_profile, user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
