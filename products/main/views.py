from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import ProductSerializer, ProductListSerializer, ProductDetailsSerializer, ReviewSerializer
from main.models import Product, Review


@api_view(['GET'])
def products_list_view(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            serializer = ProductListSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id, mark):
        reviews = Review.objects.filter(product_id=product_id, mark=mark)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
