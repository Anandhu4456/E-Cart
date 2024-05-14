from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
    return render(request, 'index.html')

def list_products(request):
    
    products = Product.objects.all
    
    return render(request, 'products_list.html',{"products":products})

def single_product(request):
    return render(request, 'product_display.html')