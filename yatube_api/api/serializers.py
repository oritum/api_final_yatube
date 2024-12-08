from posts.models import Comment, Follow, Post
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer


class PostSerializer(ModelSerializer):
    """Сериализатор модели Post."""

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = (
            'author',
            'text',
            'pub_date',
            'image',
        )
        model = Post


class CommentSerializer(ModelSerializer):
    """Сериализатор модели Comment."""

    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        fields = (
            'author',
            'post',
            'text',
            'created',
        )
        model = Comment


class FollowSerializer(ModelSerializer):
    """Сериализатор модели Follow."""

    user = SlugRelatedField(slug_field='username', read_only=True)
    following = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = (
            'user',
            'following',
        )
        model = Follow
