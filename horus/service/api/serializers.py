from rest_framework import serializers
from horus.service.models import Banks
class BanksSerializer(serializers.ModelSerializer) :
    name = serializers.CharField(null=False, min_length= 5,max_length=100)
    description= serializers.TextField(blank=True, default="No description provided")
    number = serializers.CharField(blank=True)
    location= serializers.CharField(blank=True, default="No location provided")
    link= serializers.CharField()
    fax = serializers.CharField()

    class Meta:
        model=Banks
        fields = ["name","description", "number", "location", "link", "fax"]
    def validate(self, attrs):
        if not attrs.get("name"):
            raise serializers.ValidationError({"name_error": "You didnt insert a name"})
         