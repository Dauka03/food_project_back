from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin
from .models import Picture, Shipping
# Register your models here.

@admin.register(models.foodPost)
class FoodPostAdmin(admin.ModelAdmin):
    list_display = ['title','category','cost','quantity']

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name','slug']

admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(Picture)
admin.site.register(Shipping)

