from django.contrib import admin

# Register your models here.
from .models import Product, User

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
    
    
# admin.site.register(Product, ProductAdmin)
# admin.site.register(User)



    