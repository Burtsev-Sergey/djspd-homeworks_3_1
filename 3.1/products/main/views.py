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


# доп задание:
class ProductFilteredReviews(APIView):
  def get(self, request, product_id=None):
    mark = request.query_params.get('mark', None)

    if product_id is not None:
      product = get_object_or_404(Product, pk=product_id)

      # Фильтрация отзывов по product_id и, если задано, по mark
      if mark is not None:
        try:
          mark = int(mark)
        except ValueError:
          return Response({"detail": "Invalid mark parameter"}, status=400)

        # Фильтрация по оценке
        reviews = Review.objects.filter(product=product, mark=mark)
      else:
         # Получаем все отзывы если mark не задано
        reviews = Review.objects.filter(product=product)
    else:
      # Если product_id не задан, получаем все отзывы
      if mark is not None:
        try:
          mark = int(mark)
        except ValueError:
          return Response({"detail": "Invalid mark parameter"}, status=400)

        # Получаем все отзывы с фильтрацией по оценке
        reviews = Review.objects.filter(mark=mark)
      else:
        # Получаем все отзывы без фильтрации, если mark не задано
        reviews = Review.objects.all()

    ser = ReviewSerializer(reviews, many=True)
    return Response(ser.data)