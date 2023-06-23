from django.contrib import admin

from .models import Event, EventImage, Going

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "tags"]


admin.site.register(Event, EventAdmin)
admin.site.register(EventImage)
admin.site.register(Going)
