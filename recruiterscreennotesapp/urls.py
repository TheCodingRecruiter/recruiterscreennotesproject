from django.urls import path

from .views import recruiterscreen

app_name = 'rsn'
urlpatterns = [
    path('', recruiterscreen, name='rsn'),
]