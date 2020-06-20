from django.urls import path
from . import views

urlpatterns = [
    # ACTORS
    path('actor/add/', views.AddActor.as_view(), name='add_actor'),
    path('actor/get/', views.GetAllActor.as_view(), name='get_all_actors'),
    path('actor/get/<id>/', views.GetActorWithID.as_view(), name='get_actor_with_id'),
    # PRODUCERS
    path('producer/add/', views.AddProducer.as_view(), name='add_producer'),
    path('producer/get/', views.GetAllProducer.as_view(), name='get_all_producers'),
    path('producer/get/<id>/', views.GetProducerWithID.as_view(), name='get_producer_with_id'),
    # MOVIES
    path('movie/add/', views.AddMovie.as_view(), name='add_movie'),
    path('movie/get/', views.GetAllMovie.as_view(), name='get_all_movies'),
    path('movie/get/<id>/', views.GetMovieWithID.as_view(), name='get_movie_with_id'),
]
