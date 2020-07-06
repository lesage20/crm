from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)  
    email = models.EmailField(max_length=254, null=True)
    profile_pic = models.ImageField(upload_to='user-pic', null=True, blank=True, default='images/usericon.png')
    
    date_add = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=True, null=True)
    

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    
    date_add = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=True, null=True)
    

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name
    
class Product(models.Model):
    CATEGORY=[
        ('Out  Door', 'Out  Door'),
        ('InDoor', 'InDoor')
    ]
    name = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=50, null=True, choices=CATEGORY )
    price = models.FloatField(max_length=254, null=True)
    description = models.TextField(null=True)
    tags = models.ManyToManyField(Tag)
    date_add = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=True, null=True)
    

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    
class Order(models.Model):
    STATUS = [
        ('Pending', 'Pending'),
        ('Out For Delivery', 'Out For Delivery'),
        ('Delivered', 'Delivered'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='Customer_order', null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Product_order', null=True)
    
    status = models.CharField(choices=STATUS, max_length=50, null=True)
    date_add = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")
    
    def __str__(self):
        return self.product.name




