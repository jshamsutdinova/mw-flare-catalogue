from django.contrib import admin
from catalogue.models import Catalogue

# Register your models here.

class CatalogueAdmin(admin.ModelAdmin):
    pass

admin.site.register(Catalogue, CatalogueAdmin)
