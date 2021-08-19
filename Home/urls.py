

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('forget_password/', views.forget_pasword, name='forget_password'),
    path('signin/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('shop_list/', views.shoplist, name='shop_list'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contactus/', views.contactus, name='contactus'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('adminprofile/', views.adminprofile, name='adminprofile'),
    path('admindash/', views.admindashboard, name='admindash'),
    path('add_product/', views.add_product, name='add_product'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('product_category/', views.product_category, name='product_category'),
    path('payment_method/', views.payment_method, name='payment_method'),
    path('detail/', views.detailview, name='detail'),
    path('productwishlist/', views.productwishlist, name='productwishlist'),
    path('twocolview/', views.twocolview, name='2col'),
    path('threecolview/', views.threecolview, name='3col'),
    path('fourcolview/', views.fourcolview, name='4col'),
    path('adminprofile/', views.adminprofile, name='adminprofile'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminregister/', views.adminregister, name='adminregister'),
    path('adminforgotpass/', views.adminforgotpass, name='adminforgotpass'),
    path('adminresetpass/', views.adminresetpass, name='adminresetpass'),
    path('admindash/', views.admindash, name='admindash'),
    path('adminproducts/', views.adminproducts, name='adminproducts'),
    path('admincustomers/', views.admincustomers, name='admincustomers'),
    path('adminseller/', views.adminseller, name='adminseller'),
    path('adminrating/', views.adminrating, name='adminrating'),

]