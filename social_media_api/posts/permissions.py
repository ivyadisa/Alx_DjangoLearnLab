from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Allow read-only requests for anyone. Allow write only if request.user is object's author.
    """
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS are GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        # object must have 'author' attribute
        return getattr(obj, 'author', None) == request.user
