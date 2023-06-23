from django.db import models


# Create your models here.
class HistoricalPlaceBase(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="it is historical place")
    location = models.CharField(max_length=250, default="", null=True, blank=True)
    image = models.URLField(
        default="https://egymonuments.gov.eg/en/museums/egyptian-museum"
    )

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name

    @classmethod
    def filter_by_location(cls, location: str) -> list:
        return list(cls.objects.filter(location__icontains=location))

    @classmethod
    def filter_by_name(cls, name: str) -> list:
        return list(cls.objects.filter(name__icontains=name))


class HistoricalPlace(HistoricalPlaceBase):
    service_type = models.CharField(max_length=17, default="historical_place")
    pass


class Museum(HistoricalPlaceBase):
    m_type = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    review_rate = models.IntegerField(null=True, blank=True)
    suggested_durations = models.TextField(null=True, blank=True)
    how_to_get_there = models.TextField(null=True, blank=True)
    service_type = models.CharField(max_length=10, default="museum")

    def __str__(self) -> str:
        return f"Musuem {self.name}"
