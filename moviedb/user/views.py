from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth.decorators import login_required
# Create your views here.


class RegisterView(CreateView):
    template_name = 'user/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('imdb:MovieList')

@login_required
def dashboard(request):
    return render(request,'imdb/movie_list.html',{'section': 'dashboard'})
