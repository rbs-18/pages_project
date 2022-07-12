from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class ParentWithTitle(models.Model):
    """ Parent model for all. """

    title = models.CharField(max_length=50, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class ParentContent(ParentWithTitle):
    """ Parent model for content. """

    count = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class Video(ParentContent):
    """ Model for video. """

    video_link = models.URLField()
    subtitles_link = models.URLField()


class Audio(ParentContent):
    """ Model for audio. """

    bitrate = models.DecimalField(max_digits=9, decimal_places=2)


class Text(ParentContent):
    """ Model for text. """

    describtion = models.TextField()


class Page(ParentWithTitle):
    """ Model for pages. """

    pass


class Content(models.Model):
    """ Model for content. """

    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        related_name='contents',
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ('text', 'video', 'audio')}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        content_type = str(self.content_type).split()[-1]
        return f'{content_type}: {self.content_object}'
