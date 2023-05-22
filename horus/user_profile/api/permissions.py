from rest_framework import permissions


# WARNING: THIS ONLY FOR ImageLoad
# for image load only
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_object_permission(self, request, view, obj):
        try:
            object_owner = obj.profile_picture.user
        except Exception as e:
            print(e)
            return False

        currnet_user = request.user
        print(object_owner, currnet_user)

        if object_owner == currnet_user:
            return True
        return bool(
            request.method in permissions.SAFE_METHODS
            and request.user
            and request.user.is_authenticated
        )
