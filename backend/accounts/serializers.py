from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from books.models import Category
from books.serializers import CategorySerializer, BookSerializer
from django.contrib.auth import get_user_model

class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(required=True)
    gender = serializers.ChoiceField(
        choices=[('M', '남성'), ('F', '여성')],
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    age = serializers.IntegerField(required=True)
    interested_category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        required=False,
    )
    week_avg_time = serializers.IntegerField(required=False, allow_null=True)
    year_avg_time = serializers.IntegerField(required=False, allow_null=True)
    profile_img = serializers.ImageField(required=False, allow_null=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['username'] = self.validated_data.get('username', '')
        data['gender'] = self.validated_data.get('gender', None)
        data['age'] = self.validated_data.get('age', None)
        data['week_avg_time'] = self.validated_data.get('week_avg_time', None)
        data['year_avg_time'] = self.validated_data.get('year_avg_time', None)
        data['profile_img'] = self.validated_data.get('profile_img', None)
        return data

    def save(self, request):
        user = super().save(request)
        user.username = self.validated_data.get('username', '')
        user.gender = self.validated_data.get('gender', None)
        user.age = self.validated_data.get('age', None)
        user.week_avg_time = self.validated_data.get('week_avg_time', None)
        user.year_avg_time = self.validated_data.get('year_avg_time', None)
        user.profile_img = self.validated_data.get('profile_img', None)

        user.save()

        interested_category = self.validated_data.get('interested_category', [])
        user.interested_category.set(interested_category)

        return user


User = get_user_model()
class UserSerializer(serializers.ModelSerializer):            
    interested_category = CategorySerializer(many=True)
    books = BookSerializer(many=True)
    followers_count = serializers.SerializerMethodField()
    followings_count = serializers.SerializerMethodField()
    is_followed = serializers.SerializerMethodField()
    threads_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'gender', 'age',
            'week_avg_time', 'year_avg_time',
            'profile_img', 'interested_category', 'books',
            'followers_count', 'followings_count', 'is_followed',
            'threads_count',
        ]
    
    def get_followers_count(self, obj):
        return obj.followers.count()
    
    def get_followings_count(self, obj):
        return obj.followings.count()
    
    def get_is_followed(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.followers.filter(pk=request.user.pk).exists()
        return False

    def get_threads_count(self, obj):
        return obj.thread_set.count()