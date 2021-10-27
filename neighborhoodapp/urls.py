from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name = 'index'),
    path('neighbourhood_info/(?P<id>\d+)', views.view_neighbourhood, name='view_neighbourhood'),
]