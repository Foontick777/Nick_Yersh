from django.urls import path
from .views import home, form

urlpatterns = [
    path('home/', home, name='form'),
    path('add/', form, name='page')
]