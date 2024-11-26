from django.contrib import admin
from catalogue.models import FlareList

# Register your models here.

class CatalogueAdmin(admin.ModelAdmin):
    pass

admin.site.register(FlareList, CatalogueAdmin)
