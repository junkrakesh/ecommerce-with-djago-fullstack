from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *


# Create your views here.

def home_page(request):
    return render(request,'index.html')

def about_page(request):
    return render(request,'ecommerce/about.html')

@login_required
def vendor_page(request):
    return render(request,'vendor/dashboard.html')


def products_page(request):
    context = {
        'products' : Product.objects.all()
    }
    return render(request,'ecommerce/products.html',context)

@login_required
def product_details(request,product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'item': product
    }
    return render(request,'ecommerce/productdetails.html',context)


@login_required
def custom_login_redirect(request):
    if request.user.is_staff:
        return redirect('vendor_dashboard')  # or your staff URL name
    else:
        return redirect('home')  # or your regular user URL name

@login_required
def add_to_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    user=request.user
    existingItem = Cart.objects.filter(user=user,product=product)
    if existingItem:
        messages.error(request,'Item alredy exist')
        return redirect('products-details',product_id)
    else:
        Cart.objects.create(user=user,product=product)
        messages.success(request,"item added")
        return redirect('showcart')
    
@login_required
def show_cart(request):
    cart = Cart.objects.filter(user=request.user)
    context ={
        'cartitems':cart
    }
    return render(request,'ecommerce/cart.html',context)

@login_required
def delete_cart(request,cart_id):
    cart=Cart.objects.get(id=cart_id)
    cart.delete()
    messages.success(request,'cart item deleted succesfully')
    return redirect('showcart')


@login_required
def orderItem(request,cart_id,product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                product=product,
                quantity=form.cleaned_data['quantity'],
                total_price=product.discount_price * int(form.cleaned_data['quantity']),
                address=form.cleaned_data['address'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                payment_method=form.cleaned_data['payment_method'],
                payment_status=False
            )
            if order.payment_method =='COD':
                cart = Cart.objects.get(id=cart_id)
                cart.delete()
                messages.success(request,'Order placed Succesfully')
                return redirect('home')
            elif order.payment_method == 'Card':
                pass
            else:
                messages.error(request,'Invalid order')
                return redirect('showcart')
    context = {
        'form':OrderForm
    }
    return render(request,'ecommerce/orderform.html',context)