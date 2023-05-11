from rest_framework import generics
from horus.favorites.models import Favorite
from .serializers import FavoriteSerializer
from .permissions import IsOwner
# Create your views here.
class FavoriteList(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer   

    def get_queryset(self):
        user = self.request.user
        favorites_list = Favorite.objects.filter(user=user)
        return favorites_list
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class FavoriteObject(generics.RetrieveDestroyAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = (IsOwner,)
    queryset = Favorite.objects.all()