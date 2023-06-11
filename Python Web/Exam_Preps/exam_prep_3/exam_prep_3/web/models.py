from django.db import models
from exam_prep_3.web.validators import username_min_length_validator, year_validation
from django.core.validators import MinValueValidator, MinLengthValidator


class Profile(models.Model):
    MAX_NAME_LENGTH = 30

    username = models.CharField(
        max_length=10,
        validators=[username_min_length_validator]
    )

    email = models.EmailField()

    age = models.IntegerField(
        validators=[MinValueValidator(18)]
    )

    password = models.CharField(
        max_length=MAX_NAME_LENGTH
    )

    first_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=True,
        blank=True
    )

    profile_picture = models.URLField(
        null=True,
        blank=True
    )

class Car(models.Model):
    SPORTS_CAR = 'Sports Car'
    PICK_UP = 'Pickup'
    CROSSOVER = 'Crossover'
    MINI_BUS = 'Minibus'
    OTHER = 'Other'

    CHOICES = [
        (SPORTS_CAR, SPORTS_CAR),
        (PICK_UP, PICK_UP),
        (CROSSOVER, CROSSOVER),
        (MINI_BUS, MINI_BUS),
        (OTHER, OTHER)
    ]

    type = models.CharField(
        max_length=10,
        choices=CHOICES,
    )

    model = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2)]
    )

    year = models.IntegerField(
        validators=[year_validation]
    )

    image_url = models.URLField(
        verbose_name='Image URL'
    )

    price = models.FloatField(
        validators=[MinValueValidator(1.0)]
    )