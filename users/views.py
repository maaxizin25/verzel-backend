from django.shortcuts import render
from rest_framework import generics
from users.models import User


class UserCreateView(generics.ListCreateAPIView):
    queryset=User.objects.all()


