from django.contrib import admin

from .models import Audio, Content, Page, Text, Video


class ParentContent(admin.ModelAdmin):
    """ Parent class for content. """

    search_fields = ('title',)
    exclude = ('count',)
    empty_value_display = '-empty-'


class ContentInline(admin.StackedInline):
    """ Class for inlines blocks. """

    model = Content


@admin.register(Page)
class PageAdmin(ParentContent):
    """ Class for Page admin panel. """

    list_display = ('pk', 'title')
    inlines = (ContentInline,)


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    """ Class for Content admin panel. """

    list_display = ('id', 'page', 'content_type', 'object_id', 'content_object')
    list_editable = ('page', 'object_id',)


@admin.register(Video)
class VideoAdmin(ParentContent):
    """ Class for Video admin panel. """

    list_display = ('id', 'video_link', 'subtitles_link', 'count')
    list_editable = ('video_link', 'subtitles_link')


@admin.register(Audio)
class AudioAdmin(ParentContent):
    """ Class for Audio admin panel. """

    list_display = ('id', 'title', 'bitrate', 'count')
    list_editable = ('bitrate',)


@admin.register(Text)
class TextAdmin(ParentContent):
    """ Class for Text admin panel. """

    list_display = ('id', 'title', 'describtion', 'count')
