from django.db import models
from testing_demos.web.validators import validate_phone

class Post(models.Model):
    title = models.CharField(
        max_length=30
    )
    description = models.TextField(
        max_length=500
    )
    author_name = models.CharField(
        max_length=10
    )
    author_phone = models.CharField(
        max_length=10,
        validators=validate_phone
    )
    found = models.BooleanField(
        default=False
    )