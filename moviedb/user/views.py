from django.shortcuts import render, redirect


# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views.generic import CreateView

from django.contrib import messages
from .forms import sign_up_form, login_form,user_edit_form, profile_edit_form
from .models import Profile
from  django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from user.tokens import account_activation_token
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

def user_signup(request):
    if request.method == 'POST':
        form = sign_up_form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            Profile.objects.create(user=user)
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
# ======================================================================================================

def user_login(request):
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            user_n = form.cleaned_data.get('username')
            user_p = form.cleaned_data.get('password')
            user = authenticate(request,username= user_n,password=user_p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse("Invalid login. Sign up before logging in.")
    else:
        form = login_form()
    return render(request, 'user/login.html', {'form': form})
# ========================================================================================================

@login_required #use the login_required decorator because users have to be authenticated to edit their profile
def edit(request):
    if request.method == 'POST':
        user_form = user_edit_form(request.POST, instance=request.user)
        profile_form = profile_edit_form(request.POST, instance=request.user.profile,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Congratulation.Your profile was successfully update.'))
        else:
            messages.error(request, _('Please correct the erros.'))   
    else:
        user_form = user_edit_form(instance=request.user)
        profile_form = profile_edit_form(instance=request.user.profile)
    return render(request,'user/edit.html',{'user_form': user_form,'profile_form': profile_form})
# ==========================================================================================================

class dashboard(TemplateView):
    template_name='user/dashboard.html'
    success_url = reverse_lazy('user:edit')









# class RegisterView(CreateView):
#     template_name = 'user/register.html'
#     form_class = UserCreationForm
#     success_url = reverse_lazy('imdb:MovieList')


