from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('auth/signup', signup, name='auth-signup'),
    path('auth/login', log_in, name='auth-login'),
    path('auth/logout', logout_view, name='auth-logout'),
    path('profile', profile_page, name='profile-page')
]