from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin
# Register your models here.


class FoodPostAdmin(admin.ModelAdmin):
    list_display = ['title','category','cost','quantity']
admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.foodPost,FoodPostAdmin)