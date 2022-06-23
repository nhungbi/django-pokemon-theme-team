# school_roster_app/urls.py
from django.urls import path
from . import views

app_name = "pokemon_app" #must be called app_name
urlpatterns = [
    path("", views.index, name="home"),
    path("pokemon/", views.pokemon, name="pokemon"), #id is optional as a query string
  
]