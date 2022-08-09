from rest_framework import serializers
from whatchapp.models import Movie
from .models import *









class MovieSerilizer(serializers.ModelSerializer):
    class Meta:
        models=Movie
        fields="__all__"
        # exclude=["active"]





# class MovieSerilizer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name=serializers.CharField()
#     discription=serializers.CharField()
#     active=serializers.BooleanField()



#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name",instance.name)
#         instance.discription = validated_data.get("discription",instance.discription)
#         instance.active = validated_data.get("active",instance.active)
#         instance.save()
#         return 
        
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short")  
#         else:
#             return value

#     def validate(self, data):
#         if data['name']==data['discription']:
#             raise serializers.ValidationError({"Title and Docmentations are be different"})   
#         else :
#             return data     