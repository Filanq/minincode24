from rest_framework.permissions import BasePermission


class Admin(BasePermission):
    def has_permission(self, request, view):
        try:
            return request.session['is_auth']
        except KeyError:
            return False


class Any(BasePermission):
    def has_permission(self, request, view):
        return True
