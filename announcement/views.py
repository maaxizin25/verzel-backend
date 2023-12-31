from announcement.models import Announcement
from rest_framework import generics
from announcement.serializer import AnnouncementSerializer
from announcement.permissions import AnnouncementPermissions

# Create your views here.
class AnnouncementCreateView(generics.ListCreateAPIView):
    queryset=Announcement.objects.all()
    serializer_class=AnnouncementSerializer
    permission_classes=[AnnouncementPermissions]

    def perform_create(self, serializer):
        print(self.request)
        serializer.save(user=self.request.user)
