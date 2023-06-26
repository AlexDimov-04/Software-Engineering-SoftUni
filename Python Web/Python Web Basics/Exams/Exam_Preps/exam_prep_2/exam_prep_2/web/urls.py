from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile')
    ])),
    path('plant/', include([
        path('create/', create_plant_page, name='create plant page'),
        path('details/<int:pk>', details_plant_page, name='details plant page'),
        path('edit/<int:pk>', edit_plant_page, name='edit plant page'),
        path('delete/<int:pk>', delete_plant_page, name='delete plant page'),
    ]))
]