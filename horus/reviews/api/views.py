from rest_framework import generics
from rest_framework.exceptions import ValidationError

from horus.reviews.models import ReviewBank, ReviewHotel, ReviewRestaurant

from .serializers import (
    ReviewBankSerializer,
    ReviewHotelSerializer,
    ReviewRestaurantSerializer,
)

# Create your views here.


class ReviewBankList(generics.ListCreateAPIView):
    serializer_class = ReviewBankSerializer

    def get_queryset(self):
        bank_id = self.request.query_params.get("bank_id")
        if bank_id is None:
            raise ValidationError("bank_id is required")
        return ReviewBank.get_by_bank(bank_id)


class ReviewBankObject(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewBankSerializer
    queryset = ReviewBank.objects.all()


class ReviewHotelList(generics.ListCreateAPIView):
    serializer_class = ReviewHotelSerializer

    def get_queryset(self):
        hotel_id = self.request.query_params.get("hotel_id")
        if hotel_id is None:
            raise ValidationError("hotel_id is required")
        return ReviewHotel.get_by_hotel(hotel_id)


class ReviewHotelObject(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewRestaurantSerializer
    queryset = ReviewBank.objects.all()


class ReviewRestaurantList(generics.ListCreateAPIView):
    serializer_class = ReviewRestaurantSerializer

    def get_queryset(self):
        Restaurant_id = self.request.query_params.get("Restaurant_id")
        if Restaurant_id is None:
            raise ValidationError("Restaurant_id is required")
        return ReviewRestaurant.get_by_Restaurant(Restaurant_id)


class ReviewRestaurantObject(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewRestaurantSerializer
    queryset = ReviewRestaurant.objects.all()
