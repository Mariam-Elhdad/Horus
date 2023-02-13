from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from horus.users.models import UserProfile
from .serializers import UserSerializer, UserProfileCreateSerializer, UserProfileSerializer
from rest_framework.views import APIView
User = get_user_model()


class RegisterUser(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(
                {"message": "Registered Successfully"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

   


class ProfileCreateView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileCreateSerializer
    permission_classes = (AllowAny,)

    

class UserProfileObject(APIView):
    # ---------------- helper methods ------------------- #
    def get_profile_object(self, request):
        user = request.user
        try:
            return user.profile_name
        except:
            return None
         
    # ----------------- main methods ---------------------  #
    def get(self, request):
        profile = self.get_profile_object(request)
        if profile is None:
            return Response({'details': 'the profile is not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request):
        profile = self.get_profile_object(request)
        if profile is None:
            return Response({'details': 'the profile is not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserProfileSerializer(profile, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'details', 'profile updated successfully'}, status=status.HTTP_200_OK)

    def delete(self, request):
        profile = self.get_profile_object(request)
        if profile is None:
            return Response({'details': 'the profile is not found'}, status=status.HTTP_404_NOT_FOUND)
        profile.delete()
        return Response({'details', 'profile deleted successfully'}, status=status.HTTP_200_OK)