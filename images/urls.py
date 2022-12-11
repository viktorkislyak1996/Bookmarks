from django.urls import path
from images.views import image_create

app_name = 'images'

urlpatterns = [
    # register
    path('create/', image_create, name='create'),
]
