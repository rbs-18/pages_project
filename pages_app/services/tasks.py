from celery import shared_task

from .views import increase_counters

@shared_task
def task_counter(page_id):
    increase_counters(page_id)
