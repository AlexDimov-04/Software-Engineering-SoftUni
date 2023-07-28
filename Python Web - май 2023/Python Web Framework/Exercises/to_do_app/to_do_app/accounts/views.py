from rest_framework.views import APIView
from rest_framework.authtoken import views as api_auth_views

class ApiLoginUserView(api_auth_views.ObtainAuthToken):
    pass

class ApiRegisterUserView(APIView):
    pass

class ApiLogoutUserView(APIView):
    pass