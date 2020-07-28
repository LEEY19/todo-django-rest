from rest_framework import serializers 

from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
  id = serializers.ReadOnlyField()
  class Meta:
    model = Product
    fields = ('id', 'title', 'desc', 'price', 'summary', 'featured')
    read_only_fields = ['id']

