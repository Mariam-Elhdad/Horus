from rest_framework import serializers
from horus.favorites.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = ('id', 'item_type', 'item_id')
    
