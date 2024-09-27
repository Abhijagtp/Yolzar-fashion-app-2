from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product,OrderYolzar,PayPalTransaction,OrderItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(OrderYolzar)
admin.site.register(PayPalTransaction)
admin.site.register(OrderItem)




