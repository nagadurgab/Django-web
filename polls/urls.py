from django.urls import path
from polls.views import index
urlpattrens=[
    path('',index,name='polls_list'),
    ]