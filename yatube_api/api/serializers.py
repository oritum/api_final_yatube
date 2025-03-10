"""Сериализаторы для API."""

from rest_framework.exceptions import ValidationError
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(ModelSerializer):
    """Сериализатор модели Post."""

    author = SlugRelatedField(slug_field='username', read_only=True)
    group = SlugRelatedField(
        slug_field='id',
        queryset=Group.objects.all(),
        allow_null=True,
        required=False,
    )

    class Meta:
        fields = (
            'id',
            'author',
            'text',
            'pub_date',
            'image',
            'group',
        )
        model = Post


class CommentSerializer(ModelSerializer):
    """Сериализатор модели Comment."""

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = (
            'id',
            'author',
            'post',
            'text',
            'created',
        )
        read_only_fields = (
            'id',
            'author',
            'post',
            'created',
        )
        model = Comment


class GroupSerializer(ModelSerializer):
    """Сериализатор модели Group."""

    class Meta:
        fields = (
            'id',
            'title',
            'slug',
            'description',
        )
        model = Group


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True)
    following = SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')

    def validate_following(self, value):
        request_user = self.context['request'].user
        if value == request_user:
            raise ValidationError('Нельзя подписаться на самого себя.')
        if Follow.objects.filter(user=request_user, following=value).exists():
            raise ValidationError('Вы уже подписаны на этого пользователя.')
        return value
