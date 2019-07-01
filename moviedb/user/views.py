from django.shortcuts import render, redirect


# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views.generic import CreateView

from django.contrib import messages
from .forms import sign_up_form

def signup(request):
    if request.method == 'POST':
        form = sign_up_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('imdb:MovieList')
    else:
        form = sign_up_form()
    return render(request, 'user/register.html', {'form': form})

# class RegisterView(CreateView):
#     template_name = 'user/register.html'
#     form_class = UserCreationForm
#     success_url = reverse_lazy('imdb:MovieList')


