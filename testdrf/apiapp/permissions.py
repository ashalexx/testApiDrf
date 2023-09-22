from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешить GET, HEAD или OPTIONS-запросы без ограничений.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Проверка, является ли пользователь владельцем продукта.
        return obj.owner == request.user