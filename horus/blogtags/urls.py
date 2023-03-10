from django.urls import path

from horus.blogtags.api.views import TagsView

urlpatterns = [
    path("", TagsView.as_view()),
]
