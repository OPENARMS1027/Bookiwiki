from rest_framework import serializers
from .models import Book,Category,Thread


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = '__all__'

class ThreadDetailSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    class Meta:
        model = Thread
        fields = '__all__'

class ThreadLikesSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    
    class Meta:
        model = Thread
        fields = ('id', 'likes_count', 'is_liked',)
    
    def get_likes_count(self, obj):
        return obj.likes_count()
    
    def get_is_liked(self,obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(pk=request.user.pk).exists()
        return False