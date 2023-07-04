from django.contrib import admin
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    pass