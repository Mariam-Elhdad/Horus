from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from horus.blogtags.models import Tags


class TagSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()

    class Meta:
        model = Tags
        fields = "__all__"
