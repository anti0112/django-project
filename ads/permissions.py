from users.models import User
from ads.models import Ad
from rest_framework import permissions
from ads.models import Selections
from django.http import Http404

class SelectionUpdatePermission(permissions.BasePermission):
    message = ""
    
    def has_permission(self, request, view):
        try:
            entity = Selections.objects.get(id=view.kwargs["id"])
        except Selections.DoesNotExist:
            raise Http404

        if entity.owner_id == request.user.id:
            return True
        return False
    

class AdUpdatePermission(permissions.BasePermission):
    message = "You a not permissions"
    
    def has_permission(self, request, view):
        if request.user.role in [User.MEMBER, User.ADMIN]:
            return True

        try:
            entity = Ad.objects.get(pk=view.kwargs["pk"])
        except Ad.DoesNotExist:
            raise Http404

        if entity.author_id == request.user.id:
            return True
        return False