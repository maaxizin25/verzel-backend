from django.shortcuts import render
from users.permissions import myCustomPermission
from announcement.models import Announcement
from rest_framework import generics

# Create your views here.
class AnnouncementCreateView(generics.ListCreateAPIView):
    queryset=Announcement.objects.all()
    permission_classes=[myCustomPermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
