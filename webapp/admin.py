from django.contrib import admin
from webapp.models import BeerDB

# Register your models here.

class BeerAdmin(admin.ModelAdmin):
    list_display = ['name', 'taste', 'color', 'price']


admin.site.register(BeerDB,BeerAdmin)
