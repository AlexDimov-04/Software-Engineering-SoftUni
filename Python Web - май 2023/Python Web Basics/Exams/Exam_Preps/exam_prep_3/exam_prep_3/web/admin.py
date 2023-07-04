from django.contrib import admin
from exam_prep_3.web.models import Profile, Car

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass
