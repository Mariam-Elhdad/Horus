import datetime

from django.db import models
from taggit.managers import TaggableManager

# from app.models import Tag
from horus.users.models import User

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    tags = TaggableManager()
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def going(self):
        return self.event_going.count()

    # @property
    # def insterested(self):
    #     return self.event_interested.count()

    @classmethod
    def get_comming_and_current(cls):
        return cls.objects.filter(end_at__gte=datetime.datetime.now())

    def __str__(self) -> str:
        return self.title


class EventImage(models.Model):
    image = models.ImageField(upload_to="events_images")
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="event_images"
    )

    def __str__(self) -> str:
        return str(self.image)

    @property
    def image_id(self) -> int:
        return self.id


class Going(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="event_going"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# class Interested(models.Model):
#     event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_interested')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
