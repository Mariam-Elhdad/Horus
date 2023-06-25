from django.contrib import admin

from .models import Artifact, Museum


# Register your models here.
class MuseumAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class ArtifactAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Museum, MuseumAdmin)
admin.site.register(Artifact, ArtifactAdmin)
