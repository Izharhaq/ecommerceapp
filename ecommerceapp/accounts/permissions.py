from rest_framework.permissions import BasePermission

class IsAdminOrHasEditPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_admin:
            return True
        if request.user.is_subuser:
            # Add logic to check if the user has edit permission for the specific object
            return obj.owner == request.user
        return False
