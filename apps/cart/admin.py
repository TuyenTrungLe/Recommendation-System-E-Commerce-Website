from django.contrib import admin
from .models import Sales, Cart, CartProduct, Order, Product, ProductImagesFiles, ProductImagesURL


admin.site.register([Sales, Cart, CartProduct, Order, Product])
# Register your models here.
admin.site.register(ProductImagesFiles)
admin.site.register(ProductImagesURL)