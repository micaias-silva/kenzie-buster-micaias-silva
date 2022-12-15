from rest_framework import serializers
from .models import Movie, MovieOrder, RatingChoices
from datetime import datetime
import ipdb


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_blank=True, default=None)
    rating = serializers.ChoiceField(
        choices=RatingChoices.choices, allow_blank=True, default=RatingChoices.RATED_G
    )
    synopsis = serializers.CharField(allow_blank=True, default=None)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj):
        if self.context:
            return self.context["request"].user.email

        return obj.user.email

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    buyed_by = serializers.SerializerMethodField()
    buyed_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)

    def get_title(self, obj):
        return obj.movie.title

    def get_buyed_by(self, obj):
        return obj.buyed_by.email

    def create(self, validated_data):
        # ipdb.set_trace()
        return MovieOrder.objects.create(**validated_data)
