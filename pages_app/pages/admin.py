from django.contrib import admin

from .models import Page, Video, Audio, Text, Content


class ContentInline(admin.StackedInline):
    model = Content


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    inlines = [ContentInline]


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'page', 'content_type', 'object_id', 'content_object')
    list_editable = ('page', 'object_id',)
    empty_value_display = '-empty-'


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'video_link', 'subtitles_link', 'count')
    search_fields = ('title',)
    exclude = ('count',)


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'bitrate', 'count')
    exclude = ('count',)


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'describtion', 'count')
    exclude = ('count',)
