from rest_framework import viewsets

from pages.models import Page
from .serializers import PageDetailSerializer, PageListSerializer
from services.tasks import task_counter


class PagesViewSet(viewsets.ReadOnlyModelViewSet):
    """ ViewSet for Page model. """

    queryset = Page.objects.all()
    serializer_class = PageListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return PageListSerializer
        return PageDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        task_counter.delay(instance.id)
        return super().retrieve(request, *args, **kwargs)
