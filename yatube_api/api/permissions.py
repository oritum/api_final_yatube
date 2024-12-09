"""Кастомные пермишены для API."""

from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrReadOnly(BasePermission):
    """
    Permission, позволяющий редактировать и удалять объекты только автору.
    Для остальных пользователей - только чтение.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if obj.author != request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        return True
