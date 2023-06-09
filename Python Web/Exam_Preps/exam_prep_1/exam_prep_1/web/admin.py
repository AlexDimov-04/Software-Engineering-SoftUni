from django.contrib import admin
from exam_prep_1.web.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass