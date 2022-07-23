from re import M
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
# Create your views here.

def Movielist(request):
    movie = Movie.objects.all()
    print(movie)
    data = {

               'movies':list(movie.values())
           }
    return JsonResponse(data)

def Movielists(request,pk):
    movie = Movie.objects.get(pk=pk)
    print(movie)
    data = {
                'name':movie.name,
                'discription' :movie.discription,
                'active' : movie.active,
           }
    return JsonResponse(data)    