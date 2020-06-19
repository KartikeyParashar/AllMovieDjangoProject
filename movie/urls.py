from django.urls import path
from . import views

urlpatterns = [
    path('actor/add/', views.AddActor.as_view(), name='add_actor'),
    path('actor/get/', views.GetAllActor.as_view(), name='get_all_actor'),
    path('producer/add/', views.AddProducer.as_view(), name='add_producer'),
    path('producer/get/', views.GetAllProducer.as_view(), name='get_all_producer'),
    path('movie/add/', views.AddMovie.as_view(), name='add_movie'),
]
