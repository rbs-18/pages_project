from django.db.models import F
from django.db import transaction

from pages.models import Content


def increase_counters(page_id):
    """ Increase counters. """

    with transaction.atomic():
        content_objects = Content.objects.filter(page__id=page_id)
        for obj in content_objects:
            content = obj.content_object
            content.count = F('count') + 1
            content.save()
