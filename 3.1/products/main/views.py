from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from django.shortcuts import get_object_or_404

from main.models import Review
from main.models import Product
from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer

@api_view(['GET'])
def products_list_view(request):
    products = Product.objects.all()
    ser = ProductListSerializer(products, many=True)
    return Response(ser.data)


class ProductDetailsView(APIView):
  def get(self, request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    ser = ProductDetailsSerializer(product)
    return Response(ser.data)


# class ProductDetailsView(APIView):
#     def get(self, request, product_id):
        

#         """реализуйте получение товара по id, если его нет, то выдайте 404
#         реализуйте сериализацию полученных данных
#         отдайте отсериализованные данные в Response"""
#         pass









# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        pass
