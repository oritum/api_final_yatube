from django.contrib import admin

from posts.models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """Админ-класс для сообшеств."""

    list_display = ('id', 'title', 'slug', 'description')
    search_fields = ('title',)
    list_filter = ('title',)
