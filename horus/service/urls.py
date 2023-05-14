from django.urls import path

from horus.service.api.views import (
    BankViewList,
    BankViewObject,
    HotelViewList,
    HotelViewObject,
    RestaurantViewList,
    RestaurantViewObject,
    ServicesByLocation,
)

urlpatterns = [
    path("bank/", BankViewList.as_view()),
    path("bank/<int:pk>/", BankViewObject.as_view()),
    path("restaurant/", RestaurantViewList.as_view()),
    path("restaurant/<int:pk>/", RestaurantViewObject.as_view()),
    path("hotel/", HotelViewList.as_view()),
    path("hotel/<int:pk>/", HotelViewObject.as_view()),
    path("search/location/", ServicesByLocation.as_view()),
]
