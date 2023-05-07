from rest_framework import generics
from rest_framework.exceptions import ValidationError

from horus.reviews.models import ReviewBank, ReviewHotel, ReviewRestraunt

from .serializers import (
    ReviewBankSerializer,
    ReviewHotelSerializer,
    ReviewRestrauntSerializer,
)

# Create your views here.


class ReviewBankList(generics.ListCreateAPIView):
    serializer_class = ReviewBankSerializer

    def get_queryset(self):
        bank_id = self.request.data.get("bank_id")
        if bank_id is None:
            raise ValidationError("bank_id is required")
        return ReviewBank.get_by_bank(bank_id)


class ReviewBankObject(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewBankSerializer
    queryset = ReviewBank.objects.all()


class ReviewHotelList(generics.ListCreateAPIView):
    serializer_class = ReviewHotelSerializer

    def get_queryset(self):
        hotel_id = self.request.data.get("hotel_id")
        if hotel_id is None:
            raise ValidationError("hotel_id is required")
        return ReviewHotel.get_by_hotel(hotel_id)


class ReviewHotelObject(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewRestrauntSerializer
    queryset = ReviewBank.objects.all()


class ReviewRestrauntList(generics.ListCreateAPIView):
    serializer_class = ReviewRestrauntSerializer

    def get_queryset(self):
        restraunt_id = self.request.data.get("restraunt_id")
        if restraunt_id is None:
            raise ValidationError("restraunt_id is required")
        return ReviewRestraunt.get_by_restraunt(restraunt_id)


class ReviewRestrauntObject(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewRestrauntSerializer
    queryset = ReviewRestraunt.objects.all()
