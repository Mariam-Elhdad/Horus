from rest_framework import serializers

from horus.categories.models import Category


class CategoriesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)

    class Meta:
        model = Category
        fields = ("id", "name")
