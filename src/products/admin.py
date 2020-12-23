from django.contrib import admin

from .models import Product


# Register your models here.
admin.site.register(Product)
# admin.register(Product) 这个函数没有用
