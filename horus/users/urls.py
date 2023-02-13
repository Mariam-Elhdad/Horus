from django.urls import path

from horus.users.api.views import RegisterUser
from horus.users.views import user_detail_view, user_redirect_view, user_update_view
from horus.users.api.views import ProfileCreateView, UserProfileObject

app_name = "users"
urlpatterns = [
    path("register/", RegisterUser.as_view(), name="register"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path('api/profiles/', ProfileCreateView.as_view()),
    path('api/profile/my/', UserProfileObject.as_view()),
]
