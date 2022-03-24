from rest_framework import permissions
from core.models import User, Contract

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Object-level permission to only allow users to retrieve their own information
    Anything else than a GET is denied
    """
    def has_permission(self, request, view):
        if request.method != "GET":
            return request.user.is_staff
        return True

    def has_object_permission(self, request, view, obj):
        # if admin return True
        if request.method != "GET":
            return request.user.is_staff
        
        # a GET...
        if request.user.is_staff:
            return True

        # If not admin: code dependant on object Types. We assume a "retrieve". 
        if isinstance(obj, User):
            return obj == request.user
        
        if isinstance(obj, Contract):
            return obj.clients.filter(id=request.user.id).exists()

        raise NotImplementedError("Permission not implemented for this Object Type")