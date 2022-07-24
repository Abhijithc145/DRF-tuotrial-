from rest_framework import serializers

from whatchapp.models import Movie
from .models import *

class MovieSerilizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    discription=serializers.CharField()
    active=serializers.BooleanField()



    def create(self,validated_data):
        return Movie.objects.create(**validated_data)