from django.urls import path
from .views import index, details, details_template, details_error

urlpatterns = [
    path("", index, name="index page"),
    path("int/<int:department_id>/", details, name="departments int"),
    path(
        "template/<int:department_id>/", details_template, name="departments template"
    ),
    path("error/<int:department_id>/", details_error, name="departments error"),
    path("<department_id>/", details, name="department only id"),
]


# urls_arr = ["int/<int:department_id>/", "<department_id>/"]

# urlpatterns = [path(url, details) for url in urls_arr]
