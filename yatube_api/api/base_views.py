"""Базовые представления API."""

from typing import Any

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.serializers import BaseSerializer
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsAuthorOrReadOnly


class BaseModelViewSet(ModelViewSet):
    """Кастомный базовый ViewSet."""

    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer: BaseSerializer) -> None:
        serializer.save(author=self.request.user)

    def perform_update(self, serializer: BaseSerializer) -> None:
        self.check_object_permissions(self.request, self.get_object())
        serializer.save()

    def perform_destroy(self, instance: Any) -> None:
        self.check_object_permissions(self.request, instance)
        instance.delete()
