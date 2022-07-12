from rest_framework import viewsets

from pages.models import Page
from .serializers import PageListSerializer, PageDetailSerializer
from services.views import increase_counters


class PagesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return PageListSerializer
        return PageDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        increase_counters(instance.id)
        return super().retrieve(request, *args, **kwargs)
