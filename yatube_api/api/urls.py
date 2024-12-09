from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, CommentViewSet

app_name = 'api'

router = DefaultRouter()
# router.register(r'follow', FollowListCreateView, basename='follow')
router.register('posts', PostViewSet, basename='posts')
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)

v1_urls = [
    # path('follow/', include(router.urls)),
    path('', include(router.urls)),
    path('', include('djoser.urls.jwt')),
]

urlpatterns = [
    path('v1/', include(v1_urls)),
]
