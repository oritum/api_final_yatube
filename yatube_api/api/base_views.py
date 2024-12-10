"""Базовые представления API."""

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.serializers import BaseSerializer
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsAuthorOrReadOnly


class BaseModelViewSet(ModelViewSet):
    """Кастомный базовый ViewSet."""

    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer: BaseSerializer) -> None:
        serializer.save(author=self.request.user)
