from rest_framework import serializers

from horus.museums.models import Artifact, Museum


class MuseumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Museum
        fields = "__all__"


class ArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = "__all__"


class CategorySearchSerializer(serializers.Serializer):
    category = serializers.CharField(write_only=True)
