
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from product.api.serializers import ProductSerializer
from product.models import Product , Category
from rest_framework import generics
from django.shortcuts import get_object_or_404


class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer


    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        menu = get_object_or_404(Category, pk=self.kwargs['pk'])
        products = Product.objects.filter(category=menu).filter(is_published=True)
        colors=self.request.GET.getlist('color[]')
        categories=self.request.GET.getlist('category[]')
        sezon=self.request.GET.getlist('sezon[]')
        sizes=self.request.GET.getlist('size[]')
        fit=self.request.GET.getlist('fit[]')

        if categories:
            products = products.filter(category__id__in = categories).distinct()   
        if colors:
            products = products.filter(color_name__in = colors).distinct()  
        if sezon:
            products = products.filter(sezon__in = sezon).distinct() 
        if sizes:
            products = products.filter(size__in = sizes).distinct()  
        if fit:
            products = products.filter(fit__in = fit).distinct()
        print(categories,colors,sezon, products)
        print(products,'[p')
        return products


# class ProductAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         products = Product.objects.filter(is_published=True)
#         serilizer = ProductSerializer(products, many=True)
#         return Response(data=serilizer.data, status=200)


@api_view(['GET'])
def allProducts(request):
    products = Product.objects.filter(is_published=True)
    serializer = ProductSerializer(products, many=True, context = {'request' : request})
    return Response(data=serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False, context = {'request' : request})
    return Response(data=serializer.data, status=HTTP_200_OK)


@api_view(['POST'])
def createProduct(request):
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=HTTP_201_CREATED)


@api_view(['POST'])
def updateProduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance= product, data=request.data, context = {'request' : request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteProduct(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Product succsesfully delete!')











