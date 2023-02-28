from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel

class BaseService(TimeStampedModel):
    name = models.CharField(null=False, min_length= 5,max_length=100)
    description= models.TextField(blank=True, default="No description provided")
    location= models.CharField(blank=True, default="No location provided")
    class Meta :
        abstract= True

    
class Banks(TimeStampedModel, BaseService):
    link = models.URLField()
    telephone = models.CharField(max_length=25, null=True, blank=True)


class Restaurants(TimeStampedModel, BaseService):
    telephone = models.CharField(max_length=25, null=True, blank=True)
    website = models.CharField(max_length=250, null=True, blank=True)
    open_from = models.TimeField(null=True, blank=True)
    open_to = models.TimeField(null=True, blank=True)
    rating = models.SmallIntegerField()
    cuisines = models.TextField(null=True, blank=True)
    features = models.TextField(null=True, blank=True)
    meals = models.TextField(null=True, blank=True)
    type_r = models.CharField(max_length=150, null=True, blank=True)
    menu = models.URLField(null=True, blank=True)

class Hotels(TimeStampedModel, BaseService):
    review = models.SmallIntegerField()
    cleanlinsess_review = models.SmallIntegerField(null=True, blank=True)
    service_review = models.SmallIntegerField(null=True, blank=True)
    value_review = models.SmallIntegerField(null=True, blank=True)
    language_spoken = models.CharField(max_length=200)
    