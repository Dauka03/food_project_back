from distutils.command.upload import upload
from unicodedata import category
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
        
class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        related_name = 'children',
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )
    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    def __str__(self):
        return self.name

class foodPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='articles/')
    category = models.ForeignKey(
        Category,
        related_name='foodPost',
        on_delete=models.SET_NULL,
        null=True
    )
    def __str__(self):
        return self.title
    cost = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tag, related_name='foodPost')

class Picture(models.Model):
        item = models.ImageField(upload_to='images/')
        info = models.CharField(max_length=150)

        def __str__(self):
            return str(self.pk)

class Shipping(models.Model): 
    customer = models.CharField(max_length=200, null=False) 
    ord = models.CharField(max_length=200, null=False) 
    address = models.CharField(max_length=200, null=False) 
    city = models.CharField(max_length=200, null=False) 
    state = models.CharField(max_length=200, null=False) 
    zipcode = models.CharField(max_length=200, null=False) 
    date_added = models.DateTimeField(auto_now_add=True) 
    def __str__(self): 
        return self.address 

