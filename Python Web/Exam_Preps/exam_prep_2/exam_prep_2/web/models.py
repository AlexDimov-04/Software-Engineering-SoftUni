from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

def validate_username(value):
    if value[0].islower():
        raise ValidationError("Your name must start with a capital letter!")
        
def validate_letters_only(value):
    if not value.isalpha():
        raise ValidationError("Plant name should contain only letters!")

class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(2)],
        null=False,
        blank=False
    )

    first_name = models.CharField(
        max_length=20,
        validators=[validate_username],
        null=False,
        blank=False,
        verbose_name="First Name"
    )

    last_name = models.CharField(
        max_length=20,
        validators=[validate_username],
        null=False,
        blank=False,
        verbose_name="Last Name"
    )

    profile_picture = models.URLField(
        null=True,
        blank=True
    )

class Plant(models.Model):
    OUTDOOR_PLANTS = 'Outdoor Plants'
    INDOOR_PLANTS = 'Indoor Plants'

    CHOICES = [
        (OUTDOOR_PLANTS, OUTDOOR_PLANTS),
        (INDOOR_PLANTS, INDOOR_PLANTS),
    ]

    plant_type = models.CharField(
        max_length=14,
        choices=CHOICES,
        null=False,
        blank=False,
        verbose_name="Type"
    )

    name = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2), validate_letters_only],
        null=False,
        blank=False
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Image URL"
    )

    description = models.TextField(
        null=False,
        blank=False
    )

    price = models.FloatField(
        null=False,
        blank=False
    )