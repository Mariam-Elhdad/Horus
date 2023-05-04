
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from horus.service.models import Bank, Hotel, Restraunt

@registry.register_document
class BankDocsument(Document):
    class Index:
        name = 'bank'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = Bank
         fields = [
             'name',
             'description',
         ]

@registry.register_document
class RestrauntDocsument(Document):
    class Index:
        name = 'restraunt'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = Restraunt
         fields = [
             'name',
             'description',
         ] 

@registry.register_document
class HotelDocsument(Document):
    class Index:
        name = 'hotel'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = Hotel
         fields = [
             'name',
             'description',
         ] 
         