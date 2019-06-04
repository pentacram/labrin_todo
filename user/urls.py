from django.urls import path
from django.contrib.auth import views as auth_views
from user import views as user_views
from .views import *


urlpatterns = [
    path('register/', register, name='register'),
    #path('', user_views.profile, name='profile'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', homepage, name='homepage'),
]