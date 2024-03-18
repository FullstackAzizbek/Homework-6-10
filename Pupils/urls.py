from django.urls import path
from .views import *

urlpatterns = [
    path('', pupils, name='pupils'),
    path('add_pupil', add_pupil, name='add_pupil'),
    path('<int:id>/', pupil_list, name="list_user"),
    path('delete/<int:id>/', delete_user, name='delete'),
    path('edit/<int:id>/', edit_user, name='edit'),
]
