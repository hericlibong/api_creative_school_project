from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """ Permission pour les administrateurs. """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class IsGuest(BasePermission):  
    """ Permission pour les invités (lecture seule). """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'guest'
