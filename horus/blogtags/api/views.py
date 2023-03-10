from rest_framework import generics
from rest_framework.permissions import AllowAny

from horus.blogtags.api.setializers import TagSerializer
from horus.blogtags.models import Tags


class TagsView(generics.ListAPIView, generics.ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]
