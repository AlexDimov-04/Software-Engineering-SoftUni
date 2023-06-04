from django.urls import path
from .views import index, update_task, delete_task


urlpatterns = [
    path('', index, name='list'),
    path('update_task/<pk>/', update_task, name='update_task'),
    path('delete/<pk>/', delete_task, name='delete')
]