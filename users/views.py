from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import *


class UsersView(APIView):
    def post(self, request: Request):
        user_data = request.data
        serializer = UserSerializer(data=user_data)

        if not serializer.is_valid():
            return Response(serializer.errors, 400)

        serializer.save()

        return Response(serializer.data, 201)
    