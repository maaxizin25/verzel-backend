from announcement.models import Announcement, Photos
from rest_framework import generics
from announcement.serializer import AnnouncementSerializer, PhotosSerializer
from announcement.permissions import AnnouncementPermissions, AnnouncementObjectPermissions, ImageObjectPermissions

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

class ImageDeleteView(generics.DestroyAPIView):
    queryset=Photos.objects.all()
    serializer_class=PhotosSerializer
    permission_classes=[ImageObjectPermissions]

    lookup_field= "id"
    lookup_url_kwarg = "id"
