"""Views для приложения api."""

from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from posts.models import Follow
from .serializers import FollowSerializer


class FollowListCreateView(ModelViewSet):
    """Подписка на авторов."""

    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['user__username', 'following__username']

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Подписка на автора."""
        following = serializer.validated_data['following']
        if self.request.user == following:
            raise ValidationError('Нельзя подписаться на самого себя.')
        serializer.save(user=self.request.user)
