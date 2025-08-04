from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=150,unique=True)
    slug         = models.SlugField(max_length=150,unique=True)
    description  = models.TextField(max_length=500,blank=True)
    price        = models.IntegerField()
    images       = models.ImageField(upload_to='photos/products')
    stock        = models.IntegerField()
    is_availabel = models.BooleanField(default=True)
    
    category     = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at   = models.DateTimeField(auto_now_add=True)
    modified_at  = models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse('product_details',args=[self.category.slug,self.slug]) 
    
    def __str___(self):
        return self.product_name