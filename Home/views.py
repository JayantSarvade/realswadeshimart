from django.shortcuts import render
from django.contrib import messages
from .forms import RegisterForm
# Create your views here.


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def forget_pasword(request):
    return render(request, 'forget_password.html')


def user_register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            messages.success(
                request, 'Congratulations you have signed in successful')
    else:
        register_form = RegisterForm()
    return render(request, 'register.html', {'form': register_form})


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


def my_account(request):
    return render(request, 'my_account.html')


def product_category(request):
    return render(request, 'product_category.html')


def payment_method(request):
    return render(request, 'payment_method.html')
