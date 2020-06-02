from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import UserProfile
from toolbox.models import AccessGroup
from toolbox.serializers import UserProfileSerializer


class AccessGroupsAPIView(APIView):
    """
    Returns list of Access Group items
    """

    permission_classes = (IsAuthenticated, )

    @staticmethod
    def get(request):
        """
        Calls to retrieve access groups data

        :param request: Request object

        :return: Response object
        """
        auth_user_id = int(request.GET.get('user_id'))
        user = UserProfile.objects.get(user_id=auth_user_id)
        serializer = UserProfileSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)


class AccessGroupAPIView(APIView):
    """
    Uses to change user's active group
    """

    permission_classes = (IsAuthenticated, )

    @staticmethod
    def put(request, access_group_id):
        """
        Calls to change user's active group

        :param request: Request object
        :param access_group_id: Access Group pk
        """
        user = UserProfile.objects.get(user=request.data['user_id'])
        user.active_group = AccessGroup.objects.get(id=access_group_id)
        user.save()

        return Response(status=status.HTTP_200_OK)
