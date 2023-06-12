from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):
    MIN_AGE_VALUE = 12
    MAX_LEN_CHARS = 30

    email = models.EmailField()

    age = models.IntegerField(
        validators=[MinValueValidator(MIN_AGE_VALUE)]
    )

    password = models.CharField(
        max_length=MAX_LEN_CHARS
    )

    first_name = models.CharField(
        max_length=MAX_LEN_CHARS,
        null=True,
        blank=True,
        verbose_name="First Name",
    )

    last_name = models.CharField(
        max_length=MAX_LEN_CHARS,
        null=True,
        blank=True,
        verbose_name="Last Name",
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name="Profile Picture",
    )

class Game(models.Model):
    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    PUZZLE = 'Puzzle'
    STRATEGY = 'Strategy'
    SPORTS = 'Sports'
    BOARD_CARD_GAME = 'Board/Card Game'
    OTHER = 'Other'

    CHOICES = [
        (ACTION, ACTION),
        (ADVENTURE, ADVENTURE),
        (PUZZLE, PUZZLE),
        (STRATEGY, STRATEGY),
        (SPORTS, SPORTS),
        (BOARD_CARD_GAME, BOARD_CARD_GAME),
        (OTHER, OTHER)
    ]

    title = models.CharField(
        max_length=30,
        unique=True
    )

    category = models.CharField(
        max_length=15,
        choices=CHOICES
    )

    rating = models.FloatField(
        validators=[MinValueValidator(0.1), MaxValueValidator(5.0)],
    )

    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1)],
        verbose_name='Max Level'
    )

    image_url = models.URLField(
        verbose_name='Image URL'
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )
