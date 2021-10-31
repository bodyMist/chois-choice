from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import *
from .serializer import *

# Create your views here.
class PostListAPIView(APIView):
    def get(self, request):
        serializer = PostSerializer(Posts.objects.all(), many=True)
        queryset = Posts.objects.all()
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
          	serializer.save()

class PostDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)
      
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
    
    def put(self, request, pk):
      	post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
      
    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()