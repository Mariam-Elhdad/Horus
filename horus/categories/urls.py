from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from horus.categories.api.views import CategoryView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("", CategoryView, basename="categories")


app_name = "categories"
urlpatterns = router.urls
