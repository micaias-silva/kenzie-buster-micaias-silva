from django.db import models
from datetime import datetime


class RatingChoices(models.TextChoices):
    RATED_G = "G"
    RATED_PG = "PG"
    RATED_PG_13 = "PG-13"
    RATED_R = "R"
    RATED_NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, blank=True)
    rating = models.CharField(
        max_length=20, choices=RatingChoices.choices, default=RatingChoices.RATED_G
    )
    synopsis = models.TextField(null=True, blank=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
    )
    buyers = models.ManyToManyField(
        "users.User",
        through="MovieOrder",
        # on_delete=models.CASCADE,
        related_name="buyed_movies",
    )


class MovieOrder(models.Model):
    buyed_by = models.ForeignKey("users.User", on_delete=models.CASCADE)
    buyed_at = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
