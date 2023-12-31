from rest_framework import permissions

class AnnouncementPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if(request.method == "GET"):
            return True
        elif(request.method == "POST"):
            return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated

