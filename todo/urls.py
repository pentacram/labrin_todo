from django.urls import path
from .views import *

urlpatterns = [
    path('', todo, name='todo' ),
    path('create/', create_todo, name='create_todo' ),
    path('update/<int:pk>', update_todo, name = 'update_todo'),
    path('remove/<int:pk>', del_todo, name='remove'),
    path('status/<int:pk>', todo_status, name='status')
]