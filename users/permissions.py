from rest_framework import permissions

class myCustomPermission(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
			print(request.user, obj)
			if request.method == "GET":
				return True
			return (
				request.user == obj
            )
		