from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from django.core.exceptions import ValidationError

def validate_only_alphanumeric(value):
    for ch in value:
        if not ch.isalnum() or ch != '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")

class Profile(models.Model):
    MIN_USERNAME_LENGTH = 2
    MAX_USERNAME_LENGTH = 15
    MIN_AGE_VALUE = 0

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH, 
        null=False, 
        blank=False, 
        validators=(
            MinLengthValidator(MIN_USERNAME_LENGTH),
            validate_only_alphanumeric,
        )
    )

    email = models.EmailField(
        null=False,
        blank=False
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(MIN_AGE_VALUE),
        )
    )    

class Album(models.Model):
    MAX_LENGTH_ALBUM_NAME = 30
    MAX_LENGTH_ARTIST_NAME = 30
    MAX_LENGTH_GENRE = 30

    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    RNB_MUSIC = 'R&B Music'
    ROCK_MUSIC = 'ROCK Music'
    COUNTRY_MUSIC = 'Country Music'
    DANCE_MUSIC = 'Dance Music'
    HIP_HOP_MUSIC = 'Hip Hop Music'
    OTHER_MUSIC = 'Other'

    MUSICS = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RNB_MUSIC, RNB_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
        (OTHER_MUSIC, OTHER_MUSIC),
    )
    
    album_name = models.CharField(
        max_length=MAX_LENGTH_ALBUM_NAME,
        null=False,
        blank=False,
        unique=True
    )

    artist = models.CharField(
        max_length=MAX_LENGTH_ARTIST_NAME,
        null=False,
        blank=False
    )

    genre = models.CharField(
        choices=MUSICS,
        max_length=MAX_LENGTH_GENRE,
        null=False,
        blank=False
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    image_url = models.URLField(
        null=False,
        blank=False
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(0.0),
        )
    )