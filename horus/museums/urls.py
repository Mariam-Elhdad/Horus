from django.urls import path

from horus.museums.api.views import (
    ArtifactsByCategory,
    ArtifactsList,
    ArtifactsObject,
    MuseumByLocation,
    MuseumFirst,
    MuseumList,
    MuseumObject,
)

urlpatterns = [
    path("location/", MuseumByLocation.as_view()),
    path("<int:pk>/", MuseumObject.as_view()),
    path("", MuseumList.as_view()),
    path("first/", MuseumFirst.as_view()),
    path("artifacts/", ArtifactsList.as_view()),
    path("artifacts/<int:pk>/", ArtifactsObject.as_view()),
    path("artifacts/category/", ArtifactsByCategory.as_view()),
]
