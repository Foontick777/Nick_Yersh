from django.urls import path
from homework.views import GeP

urlpatterns = [
    path('get/', GeP.as_view(), name='form'),
    path('post/', GeP.as_view(), name='post')
]