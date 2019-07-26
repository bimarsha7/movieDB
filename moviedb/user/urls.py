from django.urls import path
from django.conf.urls import url
from user import views as user_views
from django.contrib.auth.views import LoginView as login_views


app_name = 'user'

urlpatterns = [
    path('signup/', user_views.user_signup, name='signup'),
    path('login/', login_views.as_view(), name='login'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     user_views.activate, name='activate'),
    path('activate/<slug:uidb64>/<slug:token>', user_views.activate, name='activate'),
]
