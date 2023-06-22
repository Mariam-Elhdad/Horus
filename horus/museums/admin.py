from django.contrib import admin

from .models import Museum


# Register your models here.
class MuseumAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Museum, MuseumAdmin)
