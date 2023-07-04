from django.urls import path, include
from .views import photo_add, photo_details, photo_edit

urlpatterns = [
    path('add/', photo_add, name='photo add'),
    path('<int:pk>/', include([
        path('', photo_details, name='photo details'),
        path('edit/', photo_edit, name='photo edit'),
    ]))
]