from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/', views.detailview, name='detail'),
    path('cart/', views.cart, name='cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('list/', views.listview, name='list'),
    path('twocolview/', views.twocolview, name='2col'),
    path('threecolview/', views.threecolview, name='3col'),
    path('fourcolview/', views.fourcolview, name='4col'),
    path('adminprofile/', views.adminprofile, name='adminprofile'),
    path('admindash/', views.admindashboard, name='admindash'),
]
