from .models import *
from django import forms

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields = ['name','description']
        
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields = ['id','title' , 'actual_price' , 'discount_price' , 'trending' , 'tag' , 'image' , 'stock' , 'description'] 
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity','address','email','phone','payment_method']