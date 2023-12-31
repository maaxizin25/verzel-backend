from django.shortcuts import render
from rest_framework import generics
from users.models import User
from users.serializer import UserSerializer


class UserCreateView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

