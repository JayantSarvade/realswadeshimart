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
    path('my_account/', views.my_account, name='my_account'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('product_category/', views.product_category, name='product_category'),
    path('payment_method/', views.payment_method, name='payment_method'),

]
