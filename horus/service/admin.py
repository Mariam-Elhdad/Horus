from django.contrib import admin

from .models import Bank, Hotel, Restaurant


# Register your models here.
class BankAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location", "description", "link", "telephone")


class HotalAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location", "description", "review")


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location", "description", "website")


admin.site.register(Bank, BankAdmin)
admin.site.register(Hotel, HotalAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
