from django.db import models
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase


class Tags(models.Model):

    tags = TaggableManager()


class Blog(Tags, models.Model):
    pass


class TaggedBlogs(TaggedItemBase):
    content_object = models.ForeignKey("Blog", on_delete=models.CASCADE)
