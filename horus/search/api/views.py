from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SearchSerializerResponse


class searchView(APIView):
    def get(self, request):
        # using custome serializer to get each service with its resul
        result = SearchSerializerResponse.search(request)
        return Response(data=result, status=status.HTTP_200_OK)
