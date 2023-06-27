from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from horus.museums.models import Artifact, Museum

from .serializers import ArtifactSerializer, CategorySearchSerializer, MuseumSerializer


# Create your views here.
class MuseumByLocation(generics.ListAPIView):
    serializer_class = MuseumSerializer


    def get(self, request: Request, *args, **kwargs):
        location = request.query_params.get("location")
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


class MuseumFirst(generics.ListAPIView):
    serializer_class = MuseumSerializer

    def get_queryset(self):
        return Museum.objects.all()[:10]


class MuseumObject(generics.RetrieveAPIView):
    queryset = Museum.objects.all()
    serializer_class = MuseumSerializer


class ArtifactsList(generics.ListAPIView):
    serializer_class = ArtifactSerializer

    def get_queryset(self):
        return Artifact.objects.all()[:10]


class ArtifactsObject(generics.RetrieveAPIView):
    serializer_class = ArtifactSerializer
    queryset = Artifact.objects.all()


class ArtifactsByCategory(APIView):
    def get(self, request: Request):
        params = request.query_params
        serializer = CategorySearchSerializer(data=params)
        serializer.is_valid(raise_exception=True)
        result = Artifact.filter_by_category(params.get("category"))
        artifacts_serializer = ArtifactSerializer(instance=result, many=True)
        return Response(artifacts_serializer.data)
