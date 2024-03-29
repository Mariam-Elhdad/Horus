import requests
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from rest_framework import generics, mixins, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from horus.user_profile.models import ImageUpload, UserProfile

from .permissions import IsOwnerOrReadOnly
from .serializers import ImageUploadSerializer, UserProfileSerializer


# ============================== User Profile ============================  #
class UserProfileObject(APIView):
    """
    That view for retraive and update and delete the profile of current user
    methods [GET, PUT, DELETE]
    """

    # ---------------- helper methods ------------------- #
    @staticmethod
    def get_profile_object(request):
        user = request.user
        if user is not None:
            return get_object_or_404(UserProfile, user=user)
        else:
            # when the user is None there is no profile
            return None

    # ----------------- main methods ---------------------  #
    def get(self, request):
        profile = self.get_profile_object(request)
        if profile is None:
            return Response(
                {"details": "the profile is not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        profile = self.get_profile_object(request)
        if profile is None:
            return Response(
                {"details": "the profile is not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = UserProfileSerializer(profile, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(
            {"details": "profile updated successfully"}, status=status.HTTP_200_OK
        )


class UserProfileObject2(
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    """
    That view for retraive and update and delete the profile by user id
    methods [GET, PUT, DELETE]
    """

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = "user_id"

    # ------------------- static methods ---------------- #

    @staticmethod
    def is_profile_owner(request, user_id) -> bool:
        """
        return True if the current user is the profile owener else False
        """
        return request.user.id == user_id

    # -------------- main methods ------------------- #
    def get(self, request, user_id):
        if self.is_profile_owner(request, user_id):
            return redirect(reverse("profile_name:profile.me"))
        return self.retrieve(request)

    def put(self, request, user_id):
        if self.is_profile_owner(request, user_id):
            data = request.data
            headers = {"Authorization": f"JWT {self.get_token_value(request)}"}
            # TODO: change the host at production
            response = requests.put(
                "http://localhost:8000" + reverse("users:profile.me"),
                data=data,
                headers=headers,
            )

            return Response(response.json(), status=response.status_code)

        return Response(
            {"details": "you don't have permission"}, status=status.HTTP_403_FORBIDDEN
        )


# ============================== Country codes =========================== #
def get_country_codes() -> list:
    """get the country codes from other file"""
    from .CountryCodes import country_codes

    return country_codes


class CountryCodes(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response({"country_codes": get_country_codes()})


# ========================= Image upload =================================== #
class ImageUploadCreate(generics.CreateAPIView):
    queryset = ImageUpload.objects.all()
    serializer_class = ImageUploadSerializer


class ImageUploadObject(generics.RetrieveDestroyAPIView):
    queryset = ImageUpload.objects.all()
    serializer_class = ImageUploadSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    lookup_field = "id"
