from rest_framework.permissions import BasePermission
from horus.favorites.models import Favorite

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user == obj.user)