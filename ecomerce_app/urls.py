from django.urls import path
from .views import *
urlpatterns = [
    # home page urls
    path('',home_page,name='home'),
    
    # login redirect urls
    path('accounts/profile/', custom_login_redirect, name='profile_redirect'),
    
    # ecommerce page urls
    path('about/',about_page,name='about'),
    path('products/',products_page, name='products'),
    path('products/<int:product_id>/',product_details, name='products-details'),
    path('add-to-cart/<int:product_id>',add_to_cart,name='add-to-cart'),
    path('cart/',show_cart,name='showcart'),
    path('delete-cart/<int:cart_id>',delete_cart,name='delete-cart'),
    path('orderitem/<int:cart_id>/<int:product_id>',orderItem,name='orderitem'),
    
    # vendor dashboard urls
    path('vendor/dashboard',vendor_page,name='vendor_dashboard'),
    
    
]