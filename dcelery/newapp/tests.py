from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .serializers import UserSerializer
# Create your tests here.

class UserViewTests(APITestCase):
    def test_get_users(self):
        """
        Ensure we can retrieve Users list from api
        """
        url = reverse("get-users")
        
        response = self.client.get(url)

        self.assertEquals(response.status_code, status.HTTP_200_OK)