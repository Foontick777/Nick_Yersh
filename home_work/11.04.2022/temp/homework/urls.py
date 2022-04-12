from django.urls import path
from homework.views import GP

urlpatterns = [
    path('get/', GP.as_view(), name='form'),
    path('post/', GP.as_view(), name='post')
]