from django.contrib.auth import get_user_model
from django.db import models

from posts.constants import (
    SLUG_MAX_LENGTH,
    TEXT_PREVIEW_LENGTH,
    TITLLE_MAX_LENGTH,
)

User = get_user_model()


class Group(models.Model):
    """Модель сообщества."""

    title = models.CharField(
        'Название сообщества', max_length=TITLLE_MAX_LENGTH
    )
    description = models.TextField('Описание сообщества')
    slug = models.SlugField(
        'Идентификатор сообщества', max_length=SLUG_MAX_LENGTH, unique=True
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    """Модель публикации."""

    text = models.TextField('Текст публикации')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True, verbose_name='Изображение'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name='Cообщество',
    )

    def __str__(self):
        return self.text[:TEXT_PREVIEW_LENGTH]


class Comment(models.Model):
    """Модель комментария."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Публикация',
    )
    text = models.TextField('Текст комментария')
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    def __str__(self):
        return self.text[:TEXT_PREVIEW_LENGTH]


class Follow(models.Model):
    """Модель подписки пользователя на авторов."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'], name='unique_follow'
            ),
            models.CheckConstraint(
                check=~models.Q(user=models.F('following')),
                name='prevent_self_follow',
            ),
        ]

    def __str__(self):
        return f'{self.user} подписан на {self.following}'
