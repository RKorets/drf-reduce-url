from rest_framework import permissions


# if user author or admin [get-update-delete] obj permission if user not author obj only - [get]
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user or request.user.is_staff
