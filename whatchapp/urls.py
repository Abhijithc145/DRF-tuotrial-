
from .views import *
from django.urls import path

urlpatterns = [
    path("list/",Movielist,name='Movielist'),
    path("list/<int:pk>",Movielists,name='Movielists'),
    
]
