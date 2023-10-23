# from django.contrib import admin #Admin non spasial
from django.contrib.gis import admin #Admin Spasial
from .models import Facility

# Register your models here.
class LocationAdmin(admin.OSMGeoAdmin):
  default_zoom = 11
  default_lon = 18409015.29
  default_lat = 1300740.59

@admin.register(Facility)
class FacilityAdmin(LocationAdmin):
  list_filter = ['status', 'operator']
  list_display = ['id', 'name', 'status','price', 'operator']

# admin.site.register(Facility)