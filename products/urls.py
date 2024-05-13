from django.urls import path

from . import views


urlpatterns = [
    path('',views.index, name='home'),
    path('products/', views.list_products, name='list_products'),
    path('single', views.single_product, name='single_product')
]
