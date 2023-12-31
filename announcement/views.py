from users.permissions import myCustomPermission
from announcement.models import Announcement
from rest_framework import generics
from announcement.serializer import AnnouncementSerializer

# Create your views here.
class AnnouncementCreateView(generics.ListCreateAPIView):
    queryset=Announcement.objects.all()
    serializer_class=AnnouncementSerializer
    permission_classes=[myCustomPermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
