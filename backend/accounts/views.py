from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

@api_view(["GET"])
def user_info(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def this_user(request): # 현재 로그인한 사용자 정보
    serializer = UserSerializer(request.user)
    return Response(serializer.data)