from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def cart(request):
    return render(request, 'cart.html')


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


def admindashboard(request):
    return render(request, 'admindash.html')


def adminlogin(request):
    return render(request, 'adminlogin.html')


def adminregister(request):
    return render(request, 'adminregister.html')


def adminforgotpass(request):
    return render(request, 'adminforgotpass.html')


def adminresetpass(request):
    return render(request, 'adminresetpass.html')
