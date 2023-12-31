from announcement.models import Announcement
from rest_framework import generics
from announcement.serializer import AnnouncementSerializer
from announcement.permissions import AnnouncementPermissions, AnnouncementObjectPermissions

# Create your views here.
class AnnouncementCreateView(generics.ListCreateAPIView):
    queryset=Announcement.objects.all()
    serializer_class=AnnouncementSerializer
    permission_classes=[AnnouncementPermissions]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AnnouncementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Announcement.objects.all()
    serializer_class=AnnouncementSerializer
    permission_classes=[AnnouncementObjectPermissions]

    lookup_field= "id"
    lookup_url_kwarg = "id"
