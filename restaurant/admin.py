from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name',)
    list_per_page=12
    search_fields=('name',)
    
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display=('name','price','category')
    
    autocomplete_fields=('category',)
    
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    pass    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass  
@admin.register(OrderItem) 
class OrderItemAdmin(admin.ModelAdmin):
    pass   

    
    
    