from django.contrib import admin
from .models import *

# Register your models here.
class AdminCategory(admin.ModelAdmin):
    list_display=['name','created_at']
    
admin.site.register(Category, AdminCategory)


class AdminProduct(admin.ModelAdmin):
    list_display=['title','actual_price','discount_price','tag','image','description','stock','trending','created_at']
    
admin.site.register(Product, AdminProduct)

class AdminCart(admin.ModelAdmin):
    list_display=['id','user','quantity']
    
admin.site.register(Cart, AdminCart)

admin.site.register(Order)
