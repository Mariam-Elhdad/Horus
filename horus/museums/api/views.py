from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from horus.museums.models import Museum

from .serializers import MuseumSerializer


# Create your views here.
class MuseumByLocation(generics.ListAPIView):
    serializer_class = MuseumSerializer

    def get(self, request, *args, **kwargs):
        location = request.data.get("location")
        if location is None:
            return Response(
                {"detail": "you should pass location"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        museums = Museum.filter_by_location(location=location)
        serialized = self.serializer_class(museums, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


class PaginationBase(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class MuseumList(generics.ListAPIView):
    queryset = Museum.objects.all()
    serializer_class = MuseumSerializer

    def get(self, request):
        paginator = PaginationBase()
        result_page = paginator.paginate_queryset(self.queryset, request)
        serializer = MuseumSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class MuseumObject(generics.RetrieveAPIView):
    queryset = Museum.objects.all()
    serializer_class = MuseumSerializer
