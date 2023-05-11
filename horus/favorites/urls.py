from django.urls import path
from horus.favorites.api.views import FavoriteList, FavoriteObject

urlpatterns = [
    path('', FavoriteList.as_view()),
    path('<int:pk>/', FavoriteObject.as_view()),
]