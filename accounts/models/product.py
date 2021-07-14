from django.db import models
from .tag import Tag

class Product(models.Model): 
    
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )

    name= models.CharField(max_length=150, null=True) 
    price= models.DecimalField(max_digits=9, decimal_places=2, null=True)
    category= models.CharField(max_length=100, choices=CATEGORY, null=True)
    description= models.CharField(max_length=200, null=True, blank=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
