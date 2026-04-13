from django.shortcuts import render
from .models import Product, Category
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CategorySerializer, ProductSerializer



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        products = Product.objects.filter(category_id=pk)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# def product_list(request):
#     products = Product.objects.all()
#     data = [
#         {
#             "id": p.id,
#             "name": p.name,
#             "price": p.price,
#             "description": p.description,
#             "count": p.count,
#             "is_active": p.is_active,
#             "category": p.category.id
#         }
#         for p in products
#     ]
#     return JsonResponse(data, safe=False)


# def product_detail(request, id):
#     p = Product.objects.get(id=id)
#     data = {
#         "id": p.id,
#         "name": p.name,
#         "price": p.price,
#         "description": p.description,
#         "count": p.count,
#         "is_active": p.is_active,
#         "category": p.category.id
#     }
#     return JsonResponse(data)


# def category_list(request):
#     categories = Category.objects.all()
#     data = [{"id": c.id, "name": c.name} for c in categories]
#     return JsonResponse(data, safe=False)


# def category_detail(request, id):
#     c = Category.objects.get(id=id)
#     data = {"id": c.id, "name": c.name}
#     return JsonResponse(data)


# def category_products(request, id):
#     products = Product.objects.filter(category_id=id)
#     data = [
#         {
#             "id": p.id,
#             "name": p.name,
#             "price": p.price
#         }
#         for p in products
#     ]
#     return JsonResponse(data, safe=False)

# # Create your views here.
