from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from posts.models import Comment, Group, Post, Follow

User = get_user_model()


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
        fields = ('id', 'author', 'post', 'text', 'created',)
        read_only_fields = ('id', 'author', 'post', 'created',)
        model = Comment


class GroupSerializer(ModelSerializer):
    """Сериализатор модели Group."""

    class Meta:
        fields = ('id', 'title', 'slug', 'description',)
        model = Group


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True)
    following = SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ('user', 'following')

    def validate_following(self, value):
        if value == self.context['request'].user:
            raise ValidationError("Нельзя подписаться на самого себя.")
        return value

    def create(self, validated_data):
        user = self.context['request'].user
        following = validated_data['following']
        return Follow.objects.create(user=user, following=following)