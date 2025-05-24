from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from books.models import Category

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

        # M2M 필드는 save 후에 set
        interested_category = self.validated_data.get('interested_category', [])
        user.interested_category.set(interested_category)

        return user
