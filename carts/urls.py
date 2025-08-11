from django.urls import path
from . import views

urlpatterns = [
    path('',views.cart,name='carts'),
    path('add-cart/<int:product_id>/',views.add_cart,name='add_cart'),
    path('remove-cart/<int:product_id>/<int:cart_item_id>/',views.remove_cart,name='remove_cart'),
    path('remove-whole-cart/<int:product_id>/<int:cart_item_id>/',views.remove_cart_item,name='remove_whole_cart'),
]