from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(_("Categories"), max_length=100)

    def __str__(self):
        return self.name
