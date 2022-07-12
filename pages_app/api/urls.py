from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import PagesViewSet


router = DefaultRouter()
router.register('pages', PagesViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
