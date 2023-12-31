from rest_framework import permissions

class AnnouncementPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if(request.method == "GET"):
            return True
        elif(request.method == "POST"):
            return request.user.is_authenticated


class AnnouncementObjectPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if(request.method == "GET"):
            return True

        return (
            request.user.is_authenticated and obj.user == request.user
        )

class ImageObjectPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated and obj.anuncio.user == request.user
        )

