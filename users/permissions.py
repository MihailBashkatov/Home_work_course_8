from rest_framework import permissions

class ModeratorAccessPermission(permissions.BasePermission):
    message = 'Adding permissions for moderatorsd.'

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Moderators').exists()