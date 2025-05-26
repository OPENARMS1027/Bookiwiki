from rest_framework import permissions

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    # get은 누구나 접근 가능
    # delete, put은 인증된 사용자만
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return bool(request.user and request.user.is_authenticated)