from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from horus.service.models import Bank, Hotel, Restraunt

from .serializers import (
    BankSerializer,
    HotelSerializer,
    RestrauntSerializer,
    SevicesSerializer,
)


class ServicesByLocation(APIView):
    """
    get all services by the location
    """

    @staticmethod
    def is_all_services_empty(services: dict) -> bool:
        for result in services.values():
            if result:
                return False
        return True

    def get(self, request):
        serialized_services = SevicesSerializer.get_by_location(request)
        if self.is_all_services_empty(serialized_services):
            return Response(
                {"detail": "no such a loction"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            data={"services": serialized_services}, status=status.HTTP_200_OK
        )


class BankViewList(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Bank.get_by_location(self.request.data.get("location", "egypt"))


class BankViewObject(generics.RetrieveAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [AllowAny]


class HotelViewList(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Hotel.get_by_location(self.request.data.get("location", "egypt"))


class HotelViewObject(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [AllowAny]


class RestaurantViewList(generics.ListAPIView):
    queryset = Restraunt.objects.all()
    serializer_class = RestrauntSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Restraunt.get_by_location(self.request.data.get("location", "egypt"))


class RestaurantViewObject(generics.RetrieveAPIView):
    queryset = Restraunt.objects.all()
    serializer_class = RestrauntSerializer
    permission_classes = [AllowAny]
