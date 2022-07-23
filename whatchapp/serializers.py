from rest_framework import serializers


class MovieSerilizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    discription=serializers.CharField()
    active=serializers.BooleanField()