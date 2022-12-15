from rest_framework.views import APIView, Request, Response
from .models import Movie
from .serializers import MovieSerializer


class MoviesView(APIView):
    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, 200)

    def post(self, request: Request) -> Response:
        data = request.data

        serializer = MovieSerializer(data=data, context={"request": request})

        if not serializer.is_valid():
            return Response(serializer.errors, 400)

        serializer.save()

        return Response(serializer.data, 201)


class MoviesIdView(APIView):
    def delete(self, request: Request, movie_id: int) -> Response:
        try:
            movie = Movie.objects.get(id=movie_id)
            movie.delete()
            return Response(status=204)

        except Movie.DoesNotExist:
            return Response({"detail": "Not found"}, 404)
