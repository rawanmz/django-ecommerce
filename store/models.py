from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    #charField is a data type
    #db_index :You add indexes on columns when you want to speed up searches on that column. 
    # Typically, only the primary key is indexed by the database. This means look ups using the primary key are optimized.
    name=models.CharField(max_length=255,db_index=True)
    #slug is "category" in 127.0.0.1:8000/Category/
    #we can not use special charecter
    slug= models.SlugField(max_length=255,unique=True)

    class Meta:
        #set plural name for class
        verbose_name_plural = 'Categories'

    # def get_absolute_url(self):
    #     return reverse("store:category_list", args=[self.slug])

#return data from Category class
    def __str__(self):
        return self.name
    
class Product(models.Model):
    #each product must have a category
    #if delete a category all the product will also be deleted(CASCADE)
    category=models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='product_creator')
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255,default='admin')
    descreption=models.TextField(blank=True)
    #store image link
    image=models.ImageField(upload_to='images/')
    slug=models.SlugField(max_length=255)
    price=models.DecimalField(max_digits=4,decimal_places=2)
    in_stock=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        #set plural name for class
        verbose_name_plural = 'Proucuts'
        ordering=('-created',)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("store:category_list", args=[self.slug])







