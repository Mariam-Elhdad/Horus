from django.urls import path

from .api.views import (
    ReviewBankList,
    ReviewBankObject,
    ReviewHotelList,
    ReviewHotelObject,
    ReviewRestaurantList,
    ReviewRestaurantObject,
)

urlpatterns = [
    path("bank/", ReviewBankList.as_view()),
    path("bank/<int:pk>/", ReviewBankObject.as_view()),
    path("hotel/", ReviewHotelList.as_view()),
    path("hotel/<int:pk>/", ReviewHotelObject.as_view()),
    path("Restaurant/", ReviewRestaurantList.as_view()),
    path("Restaurant/<int:pk>/", ReviewRestaurantObject.as_view()),
]
