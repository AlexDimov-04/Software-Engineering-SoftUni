from django.urls import path
from django.views import generic as views
from authentication_demo.web.views import index

urlpatterns = [
    path('', index, name='index'),
]