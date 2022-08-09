from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
@api_view(['GET','POST'])
def Movielist(request):
    if request.method == "GET":
        movie = Movie.objects.all()
        serializer = MovieSerilizer(movie,many = True)
        return Response(serializer.data)


    if request.method == "POST":
        print("--------------------77777------------------------------")
        serializer = MovieSerilizer(data=request.data)
        if serializer.is_valid():
            print("--------------------88888------------------------------")
            serializer.save()
            return Response(serializer.data)  
        else:
            return Response(serializer.errors)    
            # noo  


@api_view(('GET','PUT','DELETE'))
def Movielists(request,pk):
    if request.method == "GET":
        try:
           movie = Movie.objects.get(pk=pk)
           serializer = MovieSerilizer(movie)
           return Response(serializer.data)  
        except Movie.DoesNotExist:
            return Response({'Error':'The list doesn\'t exist ' },status=status.HTTP_400_BAD_REQUEST)   


    if request.method == "PUT":
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerilizer(movie,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)        

    if request.method == "DELETE":
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
    