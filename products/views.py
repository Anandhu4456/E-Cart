from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    featured = Product.objects.order_by('priority')[:4]
    latest = Product.objects.order_by('-id')[:4]
    
    context ={
        "featured":featured,
        "latest":latest
    }
    return render(request, 'index.html',context)

def list_products(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    products = Product.objects.order_by('priority')
    pagination = Paginator(products,4)
    products = pagination.get_page(page)
    return render(request, 'products_list.html',{"products":products})

def single_product(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_display.html',{"product":product})