
from .views import *
from .import views
from django.urls import path
# from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register('stream', StreamplatformAV.as_view, basename='stream')




urlpatterns = [
    path("list/",WatchList.as_view(),name='Movielist'),
    path("list/<int:pk>",WatchLists.as_view(),name='Movielists'),
    

    # path("",include(router.urls)),
    path("stream/",Stream.as_view(),name='StreamPlatform'),
    path("stream/<int:pk>",Streams.as_view(),name='StreamPlatforms'),

    # path("stream/<int:pk>/review_create",ReviewList_Create.as_view(),name='reviewlist_create'),
    path("stream/<int:pk>/review",ReviewList.as_view(),name='reviewlist'),
    path("stream/review/<int:pk>",ReviewLists.as_view(),name='reviewlists'),
 

 # The url are change and use top twoo urls

    # path("review/",ReviewList.as_view(),name='reviewlist'),
    # path("review/<int:pk>",ReviewLists.as_view(),name='reviewlists'),



]
