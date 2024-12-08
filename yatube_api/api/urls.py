from api.views import FollowListCreateView
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register('follow', FollowListCreateView, basename='follow')

v1_urls = [
    path('follow/', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]

urlpatterns = [
    path('v1/', include(v1_urls)),
]
