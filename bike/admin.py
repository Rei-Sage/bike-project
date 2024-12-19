from django.contrib import admin
# Register your models here.
from django.utils.safestring import mark_safe
from .models import *
from bike.admin import Size
class ProductAdmin(admin.ModelAdmin):
    list_filter = ['your_existing_field']  




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

@admin.register(CategoryBike)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_product')
    list_display_links = ('id', 'name')

    def get_product(self, obj):
        return obj.product.name 
    get_product.short_description = 'Product'



@admin.register(Flag)
class FlagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    
@admin.register(FrameMaterial)
class FrameMaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    
@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    
@admin.register(Bike)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'is_published',)
    list_display_links = ('id', 'name',)
    list_filter = ('category', 'is_published',)
    search_fields = ('name', 'description',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Product_Image)
class Product_Image(admin.ModelAdmin):
    list_display = ('id','product')
    list_display_links = ('id',)
    search_fields = ('id',)

