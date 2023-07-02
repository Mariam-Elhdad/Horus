from django.urls import path

from .api.views import (
    EventList,
    EventListAll,
    EventObject,
    GoingView,
    ImageEventCreate,
    ImageEventObject,
)

urlpatterns = [
    path("", EventList.as_view()),
    path("<int:pk>/", EventObject.as_view()),
    path("all/", EventListAll.as_view()),
    path("going/", GoingView.as_view()),
    path("images/", ImageEventCreate.as_view()),
    path("images/<int:pk>/", ImageEventObject.as_view()),
]
