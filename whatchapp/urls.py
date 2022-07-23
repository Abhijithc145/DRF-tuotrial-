
from .views import *
from django.urls import path

urlpatterns = [
    path("list/",Movielist,name='Movielist'),
    
]
