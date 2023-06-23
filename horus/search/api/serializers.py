from elasticsearch_dsl import Search
from rest_framework import serializers

from horus.service.models import Bank, Hotel, Restaurant


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


class SearchRestaurantSerializer(BaseSearchSerializer):
    class Meta(BaseSearchSerializer.Meta):
        model = Restaurant


class SearchSerializerResponse:
    """
    It is class to all services
    """

    # ------------ unwanted after last update --------------- #
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

        fields = ["name", "description"]

        s = (
            Search(index=["bank", "restaurant", "hotel"])
            .query("multi_match", fields=fields, fuzziness="AUTO", query=q)
            .exclude("match", is_latest=True)
        )
        qs = s.execute()

        return [service.to_dict() for service in qs]


# def flatten(dictionary: dict) -> list:
#     array = [lst[::-1] for lst in dictionary.values() if len(lst)]
#     result = []
#     while len(array):
#         lens = {index: len(lst) for index, lst in enumerate(array)}
#         max_len = max(lens.values())
#         max_len_index = 0
#         for index, length in lens.items():
#             if length == max_len:
#                 max_len_index = index
#                 break
#         result.append(array[max_len_index].pop())
#         if len(array[max_len_index]) == 0:
#             del array[max_len_index]
#     return result
