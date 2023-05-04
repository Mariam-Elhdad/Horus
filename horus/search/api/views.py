from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SearchSerializerResponse


class searchView(APIView):
    
    def get(self, request):
        # using custome serializer to get each service with its resul
        result = SearchSerializerResponse.search(request)
        return Response(data={'services': result}, status=status.HTTP_200_OK)