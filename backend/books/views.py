from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.shortcuts import render
from .models import Book, Category, Thread
from .serializers import BookSerializer, CategorySerializer, ThreadSerializer


@api_view(["GET", "POST"])
def book_list(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def category_list(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

@api_view(["GET", "POST"])
# @permission_classes([IsAuthenticated])
def thread_list(request):
    if request.method == "GET":
        threads = Thread.objects.all()
        serializer = ThreadSerializer(threads, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ThreadSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # 프론트엔드에서 user 정보를 함께 전송하면 됩니다
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

