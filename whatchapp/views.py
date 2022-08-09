from platform import platform
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.

class WatchList(APIView):
    def get(self,request):

        movie = Watchlist.objects.all()
        serializer = WatchListSerilizer(movie,many= True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = WatchListSerilizer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    




class WatchLists(APIView):
    def get(self,request,pk):
        try:
            movie = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({'Error':'The movie is not exits'},serializer.errors)

        serializer = WatchListSerilizer(movie)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def put(self,request,pk):
        movie = Watchlist.objects.get(pk=pk)
        serializer = WatchListSerilizer(movie,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        Watchlist.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_200_OK)



class Stream(APIView):
    def get(self,request):
        platform = StreamPlatform.objects.all()
        serializer = StreamSerilizer(platform,many= True)
        return Response(serializer.data)

    def post(self,request):
        serializer = StreamSerilizer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)   
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)     

class Streams(APIView):
    def get(self,request,pk):
        platform = StreamPlatform.objects.get(pk = pk)
        serializer = StreamSerilizer(platform)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamSerilizer(platform,data= request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        StreamPlatform.objects.get(pk=pk).delete()  
        return Response(status=status.HTTP_200_OK)               