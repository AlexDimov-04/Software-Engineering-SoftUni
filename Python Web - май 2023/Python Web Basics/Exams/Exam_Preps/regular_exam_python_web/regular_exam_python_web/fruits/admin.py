from django.contrib import admin
from regular_exam_python_web.fruits.models import Profile, Fruits

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Fruits)
class FruitsAdmin(admin.ModelAdmin):
    pass
