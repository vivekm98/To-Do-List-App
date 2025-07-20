from django.urls import path,include
from .views import *

urlpatterns = [

    path('',home,name='home'),
    path('add/',add,name='add'),
    path('mark_as_done/<int:pk>/',mark_as_done,name='mark_as_done'),
    path('remove/<int:pk>/',remove,name='remove'),
    path('edit/<int:pk>/',edit,name='edit'),
    path('delete/<int:pk>/',delete,name='delete')
]