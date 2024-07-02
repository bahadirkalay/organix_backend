from django.shortcuts import render
from rest_framework.generics import ListAPIView

from post.models import Post
from post.serializers import PostSerializers
from product.models import Product
from product.serializers import ProductSerializers


# Create your views here.


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
