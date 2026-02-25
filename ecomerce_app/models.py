from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator

User = get_user_model()

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50, unique=True)
    description=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    actual_price=models.DecimalField(max_digits=15,decimal_places=2)
    discount_price=models.DecimalField(max_digits=15,decimal_places=2)
    tag=models.CharField(max_length=50)
    trending=models.BooleanField(default=False)
    image=models.ImageField(upload_to='static/uploads',blank=True)
    stock=models.IntegerField()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price
    
    def __str__(self):
        return self.product.title
    
class Order(models.Model):
    STATUS = (('In Progress','In Progress'),
              ('Way to Delivery','Way to Delivery'),
              ('Completed','Completed'))
    PAYMENTS = (('COD','COD'),
                ('Card','card'))
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2,max_digits=15)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=14,validators=[MinLengthValidator(10)])
    payment_method = models.CharField(max_length=100,choices=PAYMENTS)
    payment_status = models.BooleanField(default=False,null=True)
    order_status = models.CharField(max_length=100,choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}-{self.product.title}"