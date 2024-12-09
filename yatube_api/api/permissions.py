"""Кастомные пермишены для API."""

from typing import Any

from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.request import Request
from rest_framework.views import View


class IsAuthorOrReadOnly(BasePermission):
    """
    Permission, позволяющий редактировать и удалять объекты только автору.
    Для остальных пользователей - только чтение.
    """

    def has_object_permission(
        self, request: Request, view: View, obj: Any
    ) -> bool:
        if request.method in SAFE_METHODS:
            return True
        if obj.author != request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        return True
