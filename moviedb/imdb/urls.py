from django.urls import path
from . import views

app_name = 'imdb'
urlpatterns = [
    path('movies/', views.movie_list.as_view(), name = 'MovieList'),
    path('movie/<int:pk>', views.movie_detail.as_view(), name = 'MovieDetail')
]
