from product.models import Category
from django.db import models
from django.db.models import fields
from modeltranslation.translator import TranslationOptions, register
from product.models import Product, Category

@register(Product)
class ProductTranslation(TranslationOptions):
    fields = ('title', 'color_name', 'content', 'fit', 'sezon')

# @register(Category)
# class CategoryTranslation(TranslationOptions):
#     fields = ('title')