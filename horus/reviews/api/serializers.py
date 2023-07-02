from django.contrib.auth.models import User
from rest_framework import serializers

from horus.reviews.models import ReviewBank, ReviewHotel, ReviewRestaurant
from horus.service.models import Bank, Hotel, Restaurant


class ReviewSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        fields = ("id", "rate", "comment", "user_id")
        abstract = True

    @classmethod
    def is_user_review_before(cls, data: dict) -> bool:
        return cls.Meta.model.objects.filter(**data).exists()

    @classmethod
    def create_review(cls, user: User, validated_data: dict, service: dict):
        if cls.is_user_review_before({"user": user, **service}):
            raise serializers.ValidationError(
                f"You have already reviewed this {cls.Meta.model.__name__}!."
            )
        print(validated_data)
        instance = cls.Meta.model(user=user, **validated_data)
        instance.save()
        return instance

    @staticmethod
    def get_service_id_or_404(validated_data: dict, service_key: str) -> int:
        raise NotImplementedError("should be implemented in child class")


class ReviewBankSerializer(ReviewSerializer):
    bank_id = serializers.IntegerField(required=True)

    class Meta:
        model = ReviewBank
        fields = ReviewSerializer.Meta.fields + ("bank_id",)

    def create(self, validated_data):
        user = self.context["request"].user
        service_id = self.get_service_id_or_404(validated_data, service_key="bank_id")
        return self.create_review(user, validated_data, {"bank_id": service_id})

    @staticmethod
    def get_service_id_or_404(validated_data: dict, service_key: str) -> int:
        service_id = validated_data[service_key]
        if Bank.objects.filter(pk=service_id).exists():
            return service_id
        else:
            raise serializers.ValidationError(
                f"service with id {service_id} not found!"
            )


class ReviewHotelSerializer(ReviewSerializer):
    hotel_id = serializers.IntegerField(required=True)

    class Meta:
        model = ReviewHotel
        fields = ReviewSerializer.Meta.fields + ("hotel_id",)

    def create(self, validated_data):
        user = self.context["request"].user
        service_id = self.get_service_id_or_404(validated_data, service_key="hotel_id")
        return self.create_review(user, validated_data, {"hotel_id": service_id})

    @staticmethod
    def get_service_id_or_404(validated_data: dict, service_key: str) -> int:
        service_id = validated_data[service_key]
        print(service_id)
        if Hotel.objects.filter(pk=service_id).exists():
            return service_id
        else:
            raise serializers.ValidationError(
                f"service with id {service_id} not found!"
            )


class ReviewRestaurantSerializer(ReviewSerializer):
    Restaurant_id = serializers.IntegerField(required=True)

    class Meta:
        model = ReviewRestaurant
        fields = ReviewSerializer.Meta.fields + ("Restaurant_id",)

    def create(self, validated_data):
        user = self.context["request"].user
        print(f"valid data {validated_data}")
        service_id = self.get_service_id_or_404(
            validated_data, service_key="Restaurant_id"
        )
        return self.create_review(user, validated_data, {"Restaurant_id": service_id})

    @staticmethod
    def get_service_id_or_404(validated_data: dict, service_key: str) -> int:
        service_id = validated_data[service_key]
        if Restaurant.objects.filter(pk=service_id).exists():
            return service_id
        else:
            raise serializers.ValidationError(
                f"service with id {service_id} not found!"
            )
