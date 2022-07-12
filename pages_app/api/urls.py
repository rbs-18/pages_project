from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PagesViewSet

router = DefaultRouter()
router.register('pages', PagesViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
