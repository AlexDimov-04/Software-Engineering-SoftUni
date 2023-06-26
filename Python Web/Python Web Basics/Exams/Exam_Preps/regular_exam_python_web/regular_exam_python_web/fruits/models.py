from django.db import models
from django.core.validators import MinLengthValidator
from regular_exam_python_web.fruits.validators import first_char_validator, only_letters_validator


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[MinLengthValidator(2), first_char_validator],
    )

    last_name = models.CharField(
        max_length=35,
        validators=[MinLengthValidator(1), first_char_validator]
    )

    email = models.EmailField(
        max_length=40
    )

    password = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(8)],
    )

    image_url = models.URLField(
        null=True,
        blank=True
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        default=18
    )

class Fruits(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2), only_letters_validator]
    )

    image_url = models.URLField()

    description = models.TextField()

    nutrition = models.TextField(
        null=True,
        blank=True
    )
