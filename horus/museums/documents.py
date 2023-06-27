from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from horus.museums.models import Museum

STANDARD_FIELDS = ["id", "name", "description", "location", "image", "service_type"]


@registry.register_document
class MuseumDocsument(Document):
    class Index:
        name = "museum"

    settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Museum
        fields = STANDARD_FIELDS
