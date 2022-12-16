from rest_framework.views import APIView, Request, Response
from rest_framework.permissions import IsAuthenticated
from .models import Movie
from .serializers import MovieSerializer, MovieOrderSerializer
from rest_framework.pagination import PageNumberPagination


class MoviesView(APIView, PageNumberPagination):
    def get(self, request: Request) -> Response:
        movies = Movie.objects.all().order_by("id")

        result_page = self.paginate_queryset(movies, request, view=self)

        serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        data = request.data

        serializer = MovieSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, 400)

        serializer.save(user=request.user)

        return Response(serializer.data, 201)


class MoviesIdView(APIView):
    def delete(self, request: Request, movie_id: int) -> Response:
        try:
            movie = Movie.objects.get(id=movie_id)
            movie.delete()
            return Response(status=204)

        except Movie.DoesNotExist:
            return Response({"detail": "Not found"}, 404)


class MovieOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, movie_id: int) -> Response:
        try:
            data = request.data
            movie = Movie.objects.get(pk=movie_id)
            serializer = MovieOrderSerializer(data=data)

            if not serializer.is_valid():
                return Response(serializer.errors, 400)

            serializer.save(buyed_by=request.user, movie=movie)

            return Response(serializer.data, 201)

        except Movie.DoesNotExist:
            return Response({"detail": "Not found"})
