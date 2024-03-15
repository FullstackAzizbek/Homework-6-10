from django.urls import path
from .views import *

urlpatterns = [
    path('', pupils, name='pupils'),
    path('<int:id>/', pupil_list, name="list_user")
]
