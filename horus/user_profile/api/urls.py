from django.urls import path

from horus.user_profile.api.views import (
    CountryCodes,
    ImageUploadCreate,
    ImageUploadObject,
    UserProfileObject,
    UserProfileObject2,
)

app_name = "profile_name"

urlpatterns = [
    path("my/", UserProfileObject.as_view(), name="profile.me"),
    path("<int:user_id>/", UserProfileObject2.as_view()),
    path("country_codes/", CountryCodes.as_view()),
    path("image/create/", ImageUploadCreate.as_view()),
    path("image/<int:id>/", ImageUploadObject.as_view()),
]
