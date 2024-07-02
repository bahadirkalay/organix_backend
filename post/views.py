from django.shortcuts import render
from rest_framework.generics import ListAPIView

from post.models import Post
from post.serializers import PostSerializers


# Create your views here.


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
