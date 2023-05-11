from django.db import models
from horus.users.models import User

# Create your models here.
class Favorite(models.Model):
    user = models.ForeignKey(User, related_name='user_favorite', on_delete=models.CASCADE)
    item_type = models.CharField(max_length=250)
    item_id = models.IntegerField()
