
from .views import *
from .import views
from django.urls import path

urlpatterns = [
    path("list/",WatchList.as_view(),name='Movielist'),
    path("list/<int:pk>",WatchLists.as_view(),name='Movielists'),
    
    path("stream/",Stream.as_view(),name='StreamPlatform'),
    path("stream/<int:pk>",Streams.as_view(),name='StreamPlatforms'),

    path("review/",ReviewList.as_view(),name='reviewlist'),
    path("review/<int:pk>",ReviewLists.as_view(),name='reviewlists'),



]
