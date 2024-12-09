"""Кастомные классы пагинации для API."""

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class PostPagination(LimitOffsetPagination):
    """Пагинация для публикаций."""

    def get_paginated_response(self, data):
        return Response(
            {
                'count': self.count,
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                'results': data,
            }
        )
