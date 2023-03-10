from rest_framework import generics
from rest_framework.permissions import AllowAny

from horus.horus.blogtags.api.setializers import TagSerializer
from horus.tags.models import Tags


class TagsView(generics.ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]
