from django.contrib import admin

from .models import ReviewBank, ReviewHotel, ReviewRestaurant

# Register your models here.

admin.site.register(ReviewBank)
admin.site.register(ReviewHotel)
admin.site.register(ReviewRestaurant)
