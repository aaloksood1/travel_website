from django.contrib import admin

from .models import Destination

# Register your models here.
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'price', 'special_offer')

admin.site.register(Destination, DestinationAdmin)
