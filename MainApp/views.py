from django.shortcuts import render
from .models import Product

# Create your views here.


def Home(request):
    products = Product.objects.all().order_by('-id')[:6]
    gadgets = Product.objects.filter(category='Gadgets').order_by('-id')[:6]
    Drones = Product.objects.filter(category='Drones').order_by('-id')[:6]
    Batteries = Product.objects.filter(category='Batteries').order_by('-id')[:6]
    home = Product.objects.filter(category='Home Appliances').order_by('-id')[:6]
    auto = Product.objects.filter(category='Electric Autos').order_by('-id')[:6]
    categories = [choice[0] for choice in Product.Categories]
    context = {
        'products': products,
        'gadgets': gadgets,
        'Drones': Drones,
        'Batteries': Batteries,
        'home': home,
        'auto': auto,
        'categories': categories
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'aboutUs.html')

def Products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'product.html', context)

