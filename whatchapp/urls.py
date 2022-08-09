
from .views import *
from .import views
from django.urls import path

urlpatterns = [
    path("list/",Movielist.as_view(),name='Movielist'),
    path("list/<int:pk>",Movielists.as_view(),name='Movielists'),
    
]
