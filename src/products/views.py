from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.decorators import action
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
  queryset = models.Product.objects.all()
  serializer_class = serializers.ProductSerializer

  @action(detail=False, methods=['get'])
  def cheap_products(self, request):
    products = models.Product.objects.all().filter(price__lte=100).order_by('-price')
    serializer = self.get_serializer(products, many=True)
    return Response(serializer.data)