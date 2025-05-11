from django.contrib import admin
from . models import Product

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discount_price', 'selling_price', 'category', 'product_image']
   
