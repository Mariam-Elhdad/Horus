from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from horus.users.models import UserProfile, User, ImageUpload
from .serializers import UserSerializer, UserProfileCreateSerializer, UserProfileSerializer, \
    ImageUploadSerializer
from rest_framework.views import APIView
from rest_framework import mixins
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
import requests
from .permissions import IsOwnerOrReadOnly

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
        print(request.data)
        if profile is None:
            return Response({'details': 'the profile is not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserProfileSerializer(profile, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'details': 'profile updated successfully'}, status=status.HTTP_200_OK)

    def delete(self, request):
        profile = self.get_profile_object(request)
        if profile is None:
            return Response({'details': 'the profile is not found'}, status=status.HTTP_404_NOT_FOUND)
        profile.delete()
        return Response({'details', 'profile deleted successfully'}, status=status.HTTP_200_OK)



class UserProfileObject2(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'user_id'

    @staticmethod
    def get_token_value(request)->str:
        # 'Token 18iwejwjr9o1j'.splitez()[1]
        try:
            return request.META.get('HTTP_AUTHORIZATION').split(' ')[1] 
        except:
            return None # if not auth
    def get(self, request, user_id):
        if request.user.id == user_id:
            return redirect(reverse('users:profile.me'))
        return self.retrieve(request)
    
    def put(self, request, user_id):
        if request.user.id == user_id:
            data = request.data 
          
            headers = {'Authorization': 'JWT {}'.format(self.get_token_value(request))}           
            response = requests.put('http://localhost:8000'+reverse('users:profile.me'), data=data, headers=headers)
            
            return Response(status=response.status_code)

        return Response({'details': 'you don\'t have permission'}, status=status.HTTP_403_FORBIDDEN)
    
    def delete(self, request, user_id):
        if request.user.id == user_id:
            headers = {'Authorization': 'JWT {}'.format(self.get_token_value(request))}           
            response = requests.delete('http://localhost:8000'+reverse('users:profile.me'), headers=headers)
            
            return Response(status=response.status_code)
        return Response({'details': 'you don\'t have permission'}, status=status.HTTP_403_FORBIDDEN)


def get_country_codes() -> list:
    from .CountryCodes import country_codes
    return country_codes

class CountryCodes(APIView):
    permission_classes = (AllowAny, )
    def get(self, request):
        return Response({'country_codes': get_country_codes()})
        
class ImageUploadCreate(generics.CreateAPIView):
    queryset = ImageUpload.objects.all()
    serializer_class = ImageUploadSerializer


class ImageUploadObject(generics.RetrieveDestroyAPIView):
    queryset = ImageUpload.objects.all()
    serializer_class = ImageUploadSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    lookup_field = 'id'
    

# class ImageUploadObject(APIView):
#     # ---------------- helper methods ------------------- #
#     def get_profile(self, request):
#         user = request.user
#         if user is None:
#             return
#         return user.profile_name

#     def assign_image_to_profile(self, request, Image) -> bool: # if it assign successfully
#         profile = self.get_profile(request)
#         if profile is None:
#             return False
#         profile.picture = Image
#         profile.save()
#         return True

#     def get_image_of_user(self, id):
#         user = get_object_or_404(User, id=id)
#         profile = user.profile_name
#         if profile is None:
#             return None
#         return profile.picture

#     # ------------------ main methods -------------------- #
#     def put(self, request):
#         try:
#             file = request.data['file']
#         except KeyError:
#             return Response({'details': 'Request has no resource file attached'}, status=status.HTTP_400_BAD_REQUEST)
#         Image = ImageUpload.objects.create(image=file)
#         if self.assign_image_to_profile(request, Image) == False:
#             return Response({'details': 'may profile not found'}, status=status.HTTP_400_BAD_REQUEST)
#         return Response({'details': 'uploaded successfully', 'Image_id': Image.id}, status=status.HTTP_201_CREATED)

    
#     def get(self, request, email):
#         image = self.get_image_of_user(id)
#         if image is None:
#             return Response({'details': 'image not found or profile not exist'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = ImageUploadSerializer(image)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
    