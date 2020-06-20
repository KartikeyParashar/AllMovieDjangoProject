from django.urls import path
from . import views

urlpatterns = [
    # ACTORS
    path('actor/add/', views.AddActor.as_view(), name='add_actor'),
    path('actor/get/', views.GetAllActors.as_view(), name='get_all_actors'),
    path('actor/get/<id>/', views.GetActorWithID.as_view(), name='get_actor_with_id'),
    path('actor/update/<id>/', views.UpdateActorDetailsWithID.as_view(), name='update_actor_with_id'),
    path('actor/delete/<id>/', views.DeleteActorDetailsWithID.as_view(), name='delete_actor_with_id'),
    # PRODUCERS
    path('producer/add/', views.AddProducer.as_view(), name='add_producer'),
    path('producer/get/', views.GetAllProducers.as_view(), name='get_all_producers'),
    path('producer/get/<id>/', views.GetProducerWithID.as_view(), name='get_producer_with_id'),
    path('producer/update/<id>/', views.UpdateProducerDetailsWithID.as_view(), name='update_producer_with_id'),
    path('producer/delete/<id>/', views.DeleteProducerDetailsWithID.as_view(), name='delete_producer_with_id'),
    # MOVIES
    path('movie/add/', views.AddMovie.as_view(), name='add_movie'),
    path('movie/get/', views.GetAllMovies.as_view(), name='get_all_movies'),
    path('movie/get/<id>/', views.GetMovieWithID.as_view(), name='get_movie_with_id'),
    path('movie/update/<id>/', views.UpdateMovieDetailsWithID.as_view(), name='update_movie_with_id'),
    path('movie/delete/<id>/', views.DeleteMovieDetailsWithID.as_view(), name='delete_movie_with_id'),
]
