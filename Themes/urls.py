from django.urls import path
from .views import *

urlpatterns = [
    path('', lessons, name='lessons')
]
