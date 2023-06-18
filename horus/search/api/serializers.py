from rest_framework import serializers

from horus.search.documents import BankDocsument, HotelDocsument, RestrauntDocsument
from horus.service.models import Bank, Hotel, Restraunt


class SearchSerializer(serializers.Serializer):
    q = serializers.CharField(max_length=200)


class BaseSearchSerializer(serializers.ModelSerializer):
    service_type = serializers.SerializerMethodField()

    class Meta:
        fields = ("id", "name", "location", "description", "image", "service_type")

    def get_service_type(self, obj):
        return self.Meta.model.__name__


class SearchBankSerializer(BaseSearchSerializer):
    class Meta(BaseSearchSerializer.Meta):
        model = Bank


class SearchHotelSerializer(BaseSearchSerializer):
    class Meta(BaseSearchSerializer.Meta):
        model = Hotel


class SearchRestrauntSerializer(BaseSearchSerializer):
    class Meta(BaseSearchSerializer.Meta):
        model = Restraunt


class SearchSerializerResponse:
    """
    It is class to all services
    """

    # it is each model with its main serializer
    # must have all services or it will bring an error
    serializers = {
        Bank: SearchBankSerializer,
        Hotel: SearchHotelSerializer,
        Restraunt: SearchRestrauntSerializer,
    }

    docs = {Bank: BankDocsument, Restraunt: RestrauntDocsument, Hotel: HotelDocsument}

    @classmethod
    def search(cls, request) -> dict:
        """
        get all possible services that match query
        """
        # check the location
        search_serializer = SearchSerializer(data=request.query_params)
        search_serializer.is_valid(raise_exception=True)

        q = search_serializer.data["q"]

        result = []
        # get all services that contains location like input
        for service, doc in cls.docs.items():
            print(f"{service.__name__.lower()}.description")

            fields = ["name", "description"]
            s = (
                doc.search()
                .query("multi_match", fields=fields, fuzziness="AUTO", query=q)
                .exclude("match", is_latest=True)
            )
            # s = doc.search().query("match", description=q)
            qs = s.to_queryset()
            serializer = cls.serializers[service]
            services_match = serializer(qs, many=True)
            result.extend(list(services_match.data))

        return result
