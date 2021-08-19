

from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def forget_pasword(request):
    return render(request, 'forget_password.html')


def register(request):
    return render(request, 'register.html')


def signin(request):
    return render(request, 'signin.html')


def login(request):
    return render(request, 'login.html')


# def logout(request):
#     return render(request, 'logout.html')


def shoplist(request):
    return render(request, 'shop_list.html')


def cart(request):
    return render(request, 'cart.html')


def wishlist(request):
    return render(request, 'wishlist.html')


def checkout(request):
    return render(request, 'checkout.html')


def contactus(request):
    return render(request, 'contactus.html')


def my_orders(request):
    return render(request, 'my_orders.html')


def adminprofile(request):
    return render(request, 'adminprofile.html')


def admindashboard(request):
    return render(request, 'admindash.html')


def add_product(request):
    return render(request, 'add_product.html')


def product_category(request):
    return render(request, 'product_category.html')


def payment_method(request):
    return render(request, 'payment_method.html')



def productwishlist(request):
    return render(request, 'wishlist.html')


def detailview(request):
    return render(request, 'product.html')


def listview(request):
    return render(request, 'category-list.html')


def twocolview(request):
    return render(request, 'category-2cols.html')


def threecolview(request):
    return render(request, 'category-3cols.html')


def fourcolview(request):
    return render(request, 'category-4cols.html')


def adminprofile(request):
    return render(request, 'adminprofile.html')


def adminlogin(request):
    return render(request, 'adminlogin.html')


def adminregister(request):
    return render(request, 'adminregister.html')


def adminforgotpass(request):
    return render(request, 'adminforgotpass.html')


def adminresetpass(request):
    return render(request, 'adminresetpass.html')


def admindash(request):
    return render(request, 'admindash.html')


def adminproducts(request):
    return render(request, 'adminproducts.html')


def admincustomers(request):
    return render(request, 'admincustomers.html')


def adminseller(request):
    return render(request, 'adminseller.html')


def adminrating(request):
    return render(request, 'adminrating.html')
