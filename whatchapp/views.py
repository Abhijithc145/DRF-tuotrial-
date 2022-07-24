from django.urls import is_valid_path
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def Movielist(request):
    if request.method == "GET":
        movie = Movie.objects.all()
        serializer = MovieSerilizer(movie,many=True)
        return Response(serializer.data)


    if request.method == "POST":
        serializer = MovieSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  
        else:
            return Response(serializer.errors)    
            # noo  


@api_view(('GET',))
def Movielists(request,pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerilizer(movie)
    return Response(serializer.data)    