from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import *
from .permissions import IsUserProfile


class UsersIdView(APIView):
    permission_classes = [IsAuthenticated, IsUserProfile]

    def get(self, request: Request, user_id: int):
        user = get_object_or_404(User, id=user_id)

        self.check_object_permissions(request, user)

        serializer = UserSerializer(user)

        return Response(serializer.data)


class UsersView(APIView):
    permission_classes = []

    def post(self, request: Request):
        user_data = request.data
        serializer = UserSerializer(data=user_data)

        if not serializer.is_valid():
            return Response(serializer.errors, 400)

        serializer.save()

        return Response(serializer.data, 201)
