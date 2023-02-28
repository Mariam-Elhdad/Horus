from django.shortcuts import get_object_or_404
from rest_framework import serializers

from horus.user_profile.models import ImageUpload, UserProfile
from horus.users.models import User


class UserProfileCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()

    class Meta:
        model = UserProfile
        fields = ("date_of_birth", "phone", "code_country", "bio", "user_id")

    def create(self, validated_data):
        user = get_object_or_404(User, id=validated_data["user_id"])
        profile = UserProfile.objects.create(user=user, **validated_data)
        return profile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "date_of_birth",
            "phone",
            "code_country",
            "bio",
            "email",
            "username",
            "full_name",
        )


class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = ("image",)

    def create(self, validated_data):
        profile = self.context["request"].user.profile_name
        if profile is None:
            AssertionError("profile not found")
        image = ImageUpload.objects.create(**validated_data)
        profile.picture = image
        profile.save()
        return image
