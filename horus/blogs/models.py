from django.db import models
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase


class TaggedBlogs(TaggedItemBase):
    content_object = models.ForeignKey("Blog", on_delete=models.CASCADE)


class Blog(models.Model):

    tags = TaggableManager()
