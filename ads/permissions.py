from users.models import User
from rest_framework import permissions

class SelectionUpdatePermission(permissions.BasePermission):
    message = ""
    
    def has_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
    

class AdUpdatePermission(permissions.BasePermission):
    message = "You a not permissions"
    
    def has_permission(self, request, view, obj):
        if request.user.role in [User.MEMBER, User.ADMIN]:
            return True
        elif obj.owner == request.user:
            return True
        return False