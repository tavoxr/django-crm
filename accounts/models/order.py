from django.db import models
from .customer import Customer
from .product import Product

class Order(models.Model):
    
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    status = models.CharField(max_length=100,choices=STATUS,  null=True)
    date_created =  models.DateTimeField(auto_now_add=True, null=True)
   
    def __str__(self):
        return f'Order {self.pk}: {self.customer} {self.product} {self.status}'