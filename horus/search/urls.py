from django.urls import path
from .api.views import searchView

urlpatterns = [
    path('', searchView.as_view())
]