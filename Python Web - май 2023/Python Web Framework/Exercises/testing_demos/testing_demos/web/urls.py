from django.urls import path
from testing_demos.web.views import index

urlpatterns = [
    path('', index, name='index')
]