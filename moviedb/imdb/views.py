from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from imdb.models import Movie

class movie_list(ListView):
    model = Movie

class movie_detail(DetailView):
    model = Movie