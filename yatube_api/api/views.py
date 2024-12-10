"""Views для API."""

from typing import Optional

from rest_framework.filters import SearchFilter
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.serializers import BaseSerializer
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from api.base_views import BaseModelViewSet
from api.serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)
from posts.models import Comment, Follow, Group, Post


class PostViewSet(BaseModelViewSet):
    """ViewSet для работы с публикациями."""

    queryset = Post.objects.select_related('author', 'group').all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination


class CommentViewSet(BaseModelViewSet):
    """ViewSet для работы с комментариями."""

    serializer_class = CommentSerializer

    def get_post_id(self) -> Optional[int]:
        post_id = self.kwargs.get('post_id')
        return int(post_id) if post_id is not None else None

    def get_queryset(self):
        return Comment.objects.filter(
            post_id=self.get_post_id()
        ).select_related('author', 'post')

    def perform_create(self, serializer: BaseSerializer) -> None:
        serializer.save(
            author=self.request.user,
            post=Post.objects.get(id=self.get_post_id()),
        )


class GroupViewSet(ReadOnlyModelViewSet):
    """ViewSet для работы с сообществами."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter]
    search_fields = ['slug']


class FollowViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    """ViewSet для работы с подписками."""

    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['following__username']

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer: BaseSerializer) -> None:
        serializer.save(user=self.request.user)
