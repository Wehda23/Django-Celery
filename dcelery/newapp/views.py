from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.models import User

from .tasks import sharedtask
# Create your views here.


class UsersAPIView(APIView):
    def get(self, request):

        sharedtask.delay()
        # Get users
        users = User.objects.all()
        # serializer users
        data: list = UserSerializer(users, many= True).data
        # Return data
        return Response(data, status.HTTP_200_OK)
