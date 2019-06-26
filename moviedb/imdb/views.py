from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from imdb.models import Movie

class movie_list(ListView):
    model = Movie

