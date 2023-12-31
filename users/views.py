from django.shortcuts import render
from rest_framework import generics
from users.models import User
from users.serializer import UserSerializer


class UserCreateView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

    lookup_field= "id"
    lookup_url_kwarg = "id"