from django.urls import path
from .views import index, details, details_template

urlpatterns = [
    path("", index),
    path("int/<int:department_id>/", details),
    path("template/<int:department_id>/", details_template),
    path("<department_id>/", details)
]


# urls_arr = ["int/<int:department_id>/", "<department_id>/"]

# urlpatterns = [path(url, details) for url in urls_arr]