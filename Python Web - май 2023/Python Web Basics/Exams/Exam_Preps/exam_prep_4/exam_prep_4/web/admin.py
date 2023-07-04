from django.contrib import admin
from exam_prep_4.web.models import Profile, Game

@admin.register(Profile)
class ProfilelAdmin(admin.ModelAdmin):
    pass

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass
