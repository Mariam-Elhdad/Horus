from django.urls import path

from .api.views import (
    ReviewBankList,
    ReviewBankObject,
    ReviewHotelList,
    ReviewHotelObject,
    ReviewRestrauntList,
    ReviewRestrauntObject,
)

urlpatterns = [
    path("bank/", ReviewBankList.as_view()),
    path("bank/<int:pk>/", ReviewBankObject.as_view()),
    path("hotel/", ReviewHotelList.as_view()),
    path("hotel/<int:pk>/", ReviewHotelObject.as_view()),
    path("restraunt/", ReviewRestrauntList.as_view()),
    path("restraunt/<int:pk>/", ReviewRestrauntObject.as_view()),
]
