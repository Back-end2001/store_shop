from django.contrib import admin
from .models import Product, Category,Order,OrderItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','create_date','update_date')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('full_name','address','phone','total_price')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)