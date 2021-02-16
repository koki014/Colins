from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import (
    Category,
    Product,
    ProductImg
    
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'is_active_class', 'is_main', 'is_sub', 'is_position',)
    list_display_links = ('title','image',)
    list_filter = ('title',)
    readonly_fields = ['updated_at', 'created_at']
    search_fields = ('title', ) 
    save_on_top = True
    save_as = True #create new product easy way
    fieldsets = (
        ('Relations', {
            'fields': ('parent_category', 'related_category',),
        }),
        ('Informations', {
            'fields': ('title', 'image', 'is_active_class', 'is_main', 'is_sub', 'is_position',)
        }),
        ('Moderations', {
            'fields': ('is_published',)
        }),
    )

class ProductImgTabularInlineAdmin(admin.TabularInline):
    model = ProductImg


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('title', 'price', 'image','color_name', 'code', 'content', 'fit', 'sezon', )
    inlines = [ProductImgTabularInlineAdmin, ]
    list_display_links = ('title','price')
    list_filter = ('title',)
    search_fields = ('title', ) 
    save_on_top = True
    save_as = True #create new product easy way
    actions = ('update_product_status', )
    fieldsets = (
        ('Relations', {
            'fields': ('category', 'color'),
        }),
        ('Informations', {
            'fields': ('title', 'price', 'image', 'size', 'color_name', 'code', 'content', 'fit', 'sezon' )
        }),
        ('Moderations', {
            'fields': ('is_published',),
        }),
    )

# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImg)