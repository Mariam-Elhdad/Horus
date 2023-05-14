from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

from horus.blog.models import Post


class PostIfCreatorPermission(permissions.BasePermission):
    """
    Custom permission to only allow owners of a post to edit it.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        post = Post.objects.filter(id=request.data["post_id"]).first()
        if not post:
            return False
        return request.user == post.creator

    def has_object_permission(self, request, view, obj):
        # Check if user is the owner.

        if not request.user.is_authenticated:
            return False

        return obj.post.all().first().creator == request.user


class CreatorOrReadOnlyPermission(permissions.BasePermission):
    """
    Custom permission to only allow owners of a post to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Check if user is the owner.
        print(request.user)
        if not request.user.is_authenticated:
            return False
        print(obj.creator == request.user, request.method in SAFE_METHODS)
        return obj.creator == request.user or request.method in SAFE_METHODS
