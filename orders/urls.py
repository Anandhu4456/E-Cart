from django.urls import path
from . import views
urlpatterns = [
    path('',views.show_cart, name='show-cart'),
    path('addtocart', views.add_to_cart,name='add_to_cart'),
    path('remove/<pk>', views.remove_from_cart, name='remove'),
    path('checkout', views.checkout,name='checkout')
]
