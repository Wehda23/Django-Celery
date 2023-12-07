from django.contrib import admin
from django.urls import path
from .views import UsersAPIView

urlpatterns = [
    path("user/", UsersAPIView.as_view(), name='get-users'),
]
