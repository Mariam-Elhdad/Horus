from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from horus.service.models import Bank, Hotel, Restaurant

STANDARD_FIELDS = ["id", "name", "description", "location", "image", "service_type"]


@registry.register_document
class BankDocsument(Document):
    class Index:
        name = "bank"

    settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Bank
        fields = STANDARD_FIELDS


@registry.register_document
class RestaurantDocsument(Document):
    class Index:
        name = "restaurant"

    settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Restaurant
        fields = STANDARD_FIELDS


@registry.register_document
class HotelDocsument(Document):
    class Index:
        name = "hotel"

    settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Hotel
        fields = STANDARD_FIELDS
