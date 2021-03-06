from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name = 'index'),
    path('neighbourhood_info/(?P<id>\d+)', views.view_neighbourhood, name='view_neighbourhood'),
    path('search/', views.search, name='search'),
    path('signup/', views.signup, name='signup'),
    path('profile/',views.profile, name='profile'),
    path('update/<id>', views.update_profile, name='update_profile'),
    path('new_neighbourhood/', views.neighbourhood, name='neighbourhood'),
    path('new_post', views.new_post, name='new_post'),
    path('new_business/', views.new_business, name='new_business'),
    path('join_neighbourhood/<id>', views.join_neighbourhood, name='join_neighbourhood'),
    path('leave_neighbourhood/<id>', views.leave_neighbourhood, name='leave_neighbourhood'),
]