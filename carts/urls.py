from django.urls import path
from . import views

urlpatterns = [
    path('',views.cart,name='carts'),
    path('add-cart/<int:product_id>/',views.add_cart,name='add_cart'),
]