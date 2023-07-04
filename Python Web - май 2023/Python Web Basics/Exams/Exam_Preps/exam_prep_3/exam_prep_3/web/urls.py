from django.urls import path, include
from exam_prep_3.web.views import *


urlpatterns = [
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', profile_details, name='details profile'),
        path('edit/', profile_edit, name='edit profile'),
        path('delete/', profile_delete, name='delete profile'),
    ])),
    path('car/', include([
        path('create/', create_car, name='create car'),
        path('<int:pk>/details/', details_car, name='details car'),
        path('<int:pk>/edit/', edit_car, name='edit car'),
        path('<int:pk>/delete/', delete_car, name='delete car'),
    ]))
]