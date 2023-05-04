from rest_framework import serializers

from horus.search.documents import BankDocsument, HotelDocsument, RestrauntDocsument
from horus.service.api.serializers import (
    BankSerializer,
    HotelSerializer,
    RestrauntSerializer,
)
from horus.service.models import Bank, Hotel, Restraunt


class SearchSerializer(serializers.Serializer):
    q = serializers.CharField(max_length=200)


class SearchSerializerResponse:
    """
    It is class to all services
    """

    # it is each model with its main serializer
    # must have all services or it will bring an error
    serializers = {
        Bank: BankSerializer,
        Hotel: HotelSerializer,
        Restraunt: RestrauntSerializer,
    }

    docs = {Bank: BankDocsument, Restraunt: RestrauntDocsument, Hotel: HotelDocsument}

    @classmethod
    def search(cls, request) -> dict:
        """
        get all possible services that match query
        """
        # check the location
        search_serializer = SearchSerializer(data=request.data)
        search_serializer.is_valid(raise_exception=True)

        q = search_serializer.data["q"]

        result = {}
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
            result[service.__name__] = services_match.data

        return result
