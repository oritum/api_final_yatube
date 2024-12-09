"""Views для API."""

from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from api.base_views import BaseModelViewSet
from api.pagination import PostPagination
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
    pagination_class = PostPagination


class CommentViewSet(BaseModelViewSet):
    """ViewSet для работы с комментариями."""

    serializer_class = CommentSerializer

    def get_post_id(self):
        return self.kwargs.get('post_id')

    def get_queryset(self):
        return Comment.objects.filter(
            post_id=self.get_post_id()
        ).select_related('author', 'post')

    def perform_create(self, serializer):
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


class FollowViewSet(ModelViewSet):
    """ViewSet для работы с подписками."""

    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['following__username']

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def handle_not_allowed(self, request, *args, **kwargs):
        return Response(status=status.HTTP_404_NOT_FOUND)

    update = handle_not_allowed
    destroy = handle_not_allowed
    retrieve = handle_not_allowed
    partial_update = handle_not_allowed
