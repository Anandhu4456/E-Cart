from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return render(request, 'index.html')

def list_products(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    products = Product.objects.all()
    pagination = Paginator(products,4)
    products = pagination.get_page(page)
    return render(request, 'products_list.html',{"products":products})

def single_product(request):
    return render(request, 'product_display.html')