from django.urls import path
from .views import MoviesView, MoviesIdView, MovieOrderView

urlpatterns = [
    path("movies/", MoviesView.as_view()),
    path("movies/<int:movie_id>/", MoviesIdView.as_view()),
    path("movies/<int:movie_id>/orders/", MovieOrderView.as_view()),
]
