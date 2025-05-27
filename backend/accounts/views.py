from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserUpdateSerializer


@api_view(["GET"])
def user_info(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)
    serializer = UserSerializer(user, context={"request": request})
    return Response(serializer.data)


@api_view(["GET", "PUT"])
@permission_classes([IsAuthenticated])
def this_user(request):
    if request.method == "GET":
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = UserUpdateSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            # Return updated user data with full UserSerializer
            response_serializer = UserSerializer(
                request.user, context={"request": request}
            )
            return Response(response_serializer.data)
        return Response(serializer.errors, status=400)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def user_follow(request, user_id):
    you = get_object_or_404(get_user_model(), pk=user_id)
    me = request.user

    if you != me:
        if you.followers.filter(pk=me.pk).exists():
            you.followers.remove(me)
            is_followed = False
        else:
            you.followers.add(me)
            is_followed = True

        serializer = UserSerializer(you, context={"request": request})
        return Response(
            {"status": "success", "is_followed": is_followed, "user": serializer.data}
        )

    return Response(
        {"status": "error", "message": "자기 자신을 팔로우할 수 없습니다."}, status=400
    )
