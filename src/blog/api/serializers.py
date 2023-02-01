from rest_framework import serializers
from ..models import Post, Section

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('heading', 'body')

class PostSerializer(serializers.ModelSerializer):

    author = serializers.CharField(source='author.username')
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            'title',
            'slug',
            'author',
            'date_created',
            'type',
            'socials_image',
            'summary',
            'state',
            'sections'
        )
