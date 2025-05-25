from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Book, Category, Thread, Comment
from .serializers import BookSerializer, CategorySerializer, ThreadSerializer, ThreadDetailSerializer, CommentSerializer


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

@api_view(["GET"])
def book_detail(request, book_id):
    if request.method == "GET":
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data)

@api_view(["GET", "DELETE", "PUT",])
@permission_classes([IsAuthenticated])
def thread_detail(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    
    if request.method == "GET":
        serializer = ThreadDetailSerializer(thread)
        return Response(serializer.data)
    elif request.method == "DELETE":
        thread.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializer = ThreadSerializer(thread, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(["POST"])  
@permission_classes([IsAuthenticated])
def thread_likes(request, thread_id):
    thread = Thread.objects.get(pk=thread_id)
    if request.user in thread.likes.all():
        thread.likes.remove(request.user)
    else:
        thread.likes.add(request.user)
    serializer = ThreadSerializer(thread, context={'request': request})
    return Response(serializer.data)

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def comment_list(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    
    if request.method == "GET":
        comments = Comment.objects.filter(thread=thread).order_by('-created_at')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(
                user=request.user,
                thread=thread
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def comment_detail(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    
    if comment.user != request.user:
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
    if request.method == "GET":
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_user_books(request):
    try:
        book = Book.objects.get(id=request.data.get('book_id'))
        user = request.user

        # 이미 서재에 있는지 확인
        if user.books.filter(id=book.id).exists():
            return Response(
                {'message': 'already_exists'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        # 서재에 추가
        user.books.add(book)
        return Response({'message': 'success'}, status=status.HTTP_201_CREATED)

    except Book.DoesNotExist:
        return Response(
            {'message': 'book_not_found'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            {'message': str(e)}, 
            status=status.HTTP_400_BAD_REQUEST
        )
