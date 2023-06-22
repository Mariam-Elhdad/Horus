from django.urls import path

from horus.museums.api.views import MuseumByLocation, MuseumList, MuseumObject

urlpatterns = [
    path("location/", MuseumByLocation.as_view()),
    path("<int:pk>/", MuseumObject.as_view()),
    path("", MuseumList.as_view()),
]
