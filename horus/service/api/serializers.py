from rest_framework import serializers

from horus.service.models import Bank, BaseService, Hotel, Restaurant


class BaseServiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, read_only=True)
    location = serializers.CharField(max_length=200, read_only=True)
    image = serializers.URLField(read_only=True)
    description = serializers.CharField(read_only=True)

    class Meta:
        abstract = True


class BankSerializer(BaseServiceSerializer):
    link = serializers.URLField(read_only=True)
    telephone = serializers.CharField(max_length=25)

    class Meta:
        model = Bank
        fields = "__all__"


class HotelSerializer(BaseServiceSerializer):
    review = serializers.IntegerField(read_only=True)
    cleanlinsess_review = serializers.IntegerField(read_only=True)
    service_review = serializers.IntegerField(read_only=True)
    value_review = serializers.IntegerField(read_only=True)
    language_spoken = serializers.CharField(read_only=True)

    class Meta:
        model = Hotel
        fields = "__all__"


class RestaurantSerializer(BaseServiceSerializer):
    telephone = serializers.CharField(read_only=True)
    website = serializers.CharField(read_only=True)
    open_from = serializers.TimeField(read_only=True)
    open_to = serializers.TimeField(read_only=True)
    rating = serializers.IntegerField(read_only=True)
    cuisines = serializers.CharField(read_only=True)
    features = serializers.CharField(read_only=True)
    meals = serializers.CharField(read_only=True)
    type_r = serializers.CharField(read_only=True)
    menu = serializers.URLField(read_only=True)

    class Meta:
        model = Restaurant
        fields = "__all__"


class LocationSerializer(serializers.Serializer):
    location = serializers.CharField(max_length=200)


class SevicesSerializer:
    """
    It is class to all services
    """

    # it is each model with its main serializer
    # must have all services or it will bring an error
    serializers = {
        Bank: BankSerializer,
        Hotel: HotelSerializer,
        Restaurant: RestaurantSerializer,
    }

    @classmethod
    def serialize_service(
        cls, service: BaseService, objects: list
    ) -> BaseServiceSerializer:
        service_serializer = cls.serializers.get(service, None)
        if service_serializer is None:
            raise NotImplementedError(
                f"should add {service} to serializers dict in {cls.__name__} class"
            )
        return service_serializer(objects, many=True)

    @classmethod
    def get_by_location(cls, request) -> dict:
        """
        get all possible services that have this location
        """
        # check the location
        location_serializer = LocationSerializer(data=request.data)
        location_serializer.is_valid(raise_exception=True)

        # get all services that contains location like input
        services = BaseService.get_all_services_by_location(
            location_serializer.validated_data["location"]
        )
        serialized_services = {}
        for service, objects in services.items():
            serializer = cls.serialize_service(service, objects)
            serialized_services[service.__name__] = serializer.data
        return serialized_services
