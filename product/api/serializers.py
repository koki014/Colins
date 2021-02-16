from django.db.models import fields
from rest_framework import serializers
from product.models import Product



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'price',
            'image',
            'size',
            'color_name',
            'code',
            'content',
            'fit',
            'sezon',
            'category',
            'color',
            'created_at'

        )
        
    def to_representation(self, instance):
        data = super(ProductSerializer, self).to_representation(instance)
        # manipulate data here 
        return data


# class CreateProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = (
#             'id',
#             'title',
#             'price',
#             'image',
#             'size',
#             'color_name',
#             'code',
#             'content',
#             'fit',
#             'sezon',
#             'category',
#             'color',
#             'created_at'

#         )