from rest_framework import serializers
from .models import Book, Category, Thread, Comment


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ThreadSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    class Meta:
        model = Thread
        fields = '__all__'
        
class ThreadCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = '__all__'

class ThreadDetailSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    class Meta:
        model = Thread
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'thread', 'created_at', 'updated_at')
        read_only_fields = ('id', 'user', 'thread', 'created_at', 'updated_at')
