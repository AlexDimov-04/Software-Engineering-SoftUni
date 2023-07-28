from django.urls import path
from to_do_app.accounts.views import ApiRegisterUserView, ApiLoginUserView, ApiLogoutUserView


urlpatterns = [
    path('register/', ApiRegisterUserView.as_view(), name='api_register_view'),
    path('login/', ApiLoginUserView.as_view(), name='api_login_view'),
    path('logout/', ApiLogoutUserView.as_view(), name='api_logout_view'),
]