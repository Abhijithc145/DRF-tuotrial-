from operator import is_
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.

class Movielist(APIView):
    def get(self,request):

        movie = Movie.objects.all()
        serializer = MovieSerilizer(movie,many= True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = MovieSerilizer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    




class Movielists(APIView):
    def get(self,request,pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error':'The movie is not exits'},serializer.errors)

        serializer = MovieSerilizer(movie)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def put(self,request,pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerilizer(movie,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        Movie.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_200_OK)