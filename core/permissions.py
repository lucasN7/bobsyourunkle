from rest_framework import permissions
from core.models import User, Contract

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    1. Admins have all rights
    2. Object-level permission to only allow clients to retrieve their own information
    - PATCH is allowed for contract resiliation
    - GET are allowed, data is restricted (here or in get_queryset)
    - other methods are denied for clients
    """
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if request.method not in ["GET", "PATCH"]:
            return False
        return True

    def has_object_permission(self, request, view, obj):

        if request.user.is_staff:
            return True
        
        if isinstance(obj, User):
            return obj == request.user
        
        if isinstance(obj, Contract):
            return obj.clients.filter(id=request.user.id).exists()

        raise NotImplementedError("Permission not implemented for this Object Type")