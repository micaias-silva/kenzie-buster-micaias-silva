from django.urls import path
from .views import MoviesView, MoviesIdView

urlpatterns = [
    path("movies/", MoviesView.as_view()),
    path("movies/<int:movie_id>/", MoviesIdView.as_view()),
]
