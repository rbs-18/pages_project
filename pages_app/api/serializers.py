from generic_relations.relations import GenericRelatedField
from rest_framework import serializers

from pages.models import Audio, Content, Page, Text, Video


class ContentSerializer(serializers.ModelSerializer):
    """ Serializer for content in list presentation Page's model. """

    content_type = serializers.StringRelatedField()

    class Meta:
        model = Content
        fields = ('content_type',)


class PageListSerializer(serializers.ModelSerializer):
    """ Serializer for list presentation model Page. """

    contents = ContentSerializer(many=True, required=False)
    detail_information = serializers.HyperlinkedIdentityField(
        read_only=True,
        view_name='page-detail',
    )

    class Meta:
        model = Page
        fields = ('id', 'title', 'detail_information', 'contents')


class AudioSerializer(serializers.ModelSerializer):
    """ Serializer for Audio model. """

    class Meta:
        model = Audio
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    """ Serializer for Video model. """

    class Meta:
        model = Video
        fields = '__all__'


class TextSerializer(serializers.ModelSerializer):
    """ Serializer for Text model. """

    class Meta:
        model = Text
        fields = '__all__'


class ContentDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for mapping all possible models to their
    respective serializers.
    """

    content_type = serializers.StringRelatedField()
    content_object = GenericRelatedField(
        {
            Audio: AudioSerializer(),
            Video: VideoSerializer(),
            Text: TextSerializer(),
        }
    )

    class Meta:
        model = Content
        fields = ('content_type', 'content_object',)


class PageDetailSerializer(serializers.ModelSerializer):
    """ Serializer for detail presentation of model Page. """

    contents = ContentDetailSerializer(many=True, required=False)

    class Meta:
        model = Page
        fields = ('id', 'title', 'contents')
