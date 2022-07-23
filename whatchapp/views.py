from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view()
def Movielist(request):
    movie = Movie.objects.all()
    serializer = MovieSerilizer(movie,many=True)
    return Response(serializer.data)


@api_view(('GET',))
def Movielists(request,pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerilizer(movie)
    return Response(serializer.data)    