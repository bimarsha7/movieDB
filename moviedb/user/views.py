from django.shortcuts import render, redirect


# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views.generic import CreateView

from django.contrib import messages
from .forms import sign_up_form
from  django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from user.tokens import account_activation_token
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = sign_up_form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = "Activate your MovieDB account"
            # username = form.cleaned_data.get('username')
            message = render_to_string('user/acc_activate_email.html',{
                'user' : user,
                'domain' : current_site.domain,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            # messages.success(request, f'Account created for {username}!')
            # user.email_user(subject, message)
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(subject=subject, body=message, to=[to_email])
            email.send()
            return HttpResponse('please confirm your email address')
    else:
        form = sign_up_form()
    return render(request, 'user/signup.html', {'form': form})

# =================================================================================================

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError):
        print("User does not exist")
        user = None

    if user is not None and account_activation_token.check_token(user,token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('imdb:MovieList')
    else:
        return HttpResponse("Activation link is Invalid...!!!")






# class RegisterView(CreateView):
#     template_name = 'user/register.html'
#     form_class = UserCreationForm
#     success_url = reverse_lazy('imdb:MovieList')


