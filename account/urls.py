from django.urls import path
from account.views import *


urlpatterns = [
    path('login/', user_login, name='login')
]