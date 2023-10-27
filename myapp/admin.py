from django.contrib import admin

# Register your models here.
from .models import Product, User, Order

@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    ordering = ['name', '-price']
    list_filter = ['description']
    search_fields = ['name']
    search_help_text = 'Поиск по наименованию продукта'
    actions = [reset_quantity]
    fields = ['name', 'description', 'quantity', 'image']
 
 
@admin.register(User)
class UserAdmin(admin.ModelAdmin):   
    list_display = ['name', 'email', 'phone_number', 'adress']
    ordering = ['name', 'email']
    list_filter = ['name']
    search_fields = ['name']
    search_help_text = 'Поиск по имени клиента'
    fields = ['name', 'email', 'adress', 'phone_number']
    
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):   
    list_display = ['customer', 'date_ordered', 'total_price'] # must not be a ManyToManyField
    ordering = ['customer', 'total_price'] #
    list_filter = ['customer', 'products']
    search_fields = ['products']
    search_help_text = 'Поиск по товарам в корзине'
    fields = ['customer', 'date_ordered', 'total_price'] #cannot include the ManyToManyField 'products', because that field manually specifies a relationship model
        
    
    
# admin.site.register(Product, ProductAdmin)
# admin.site.register(User)



    