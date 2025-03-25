from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from main.models import Review, Product, MarkChoices
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
        """Фильтрация отзывов по оценке и продукту."""
        mark = request.query_params.get('mark')

        filter_kwargs = {}
        if product_id is not None:
            filter_kwargs["product_id"] = product_id

        if mark:
            if not mark.isdigit():
                return Response({"detail": "Invalid mark parameter"}, status=400)

            mark = int(mark)
            if mark not in MarkChoices.values:
                return Response({"detail": f"Mark must be between {MarkChoices.VERY_BAD} and {MarkChoices.PERFECT}"}, status=400)

            filter_kwargs["mark"] = mark

        reviews = Review.objects.filter(**filter_kwargs)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)