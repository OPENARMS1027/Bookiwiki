from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.book_list),
    path("books/<int:book_id>/", views.book_detail),
    path("categories/", views.category_list),
    path("threads/", views.thread_list),
    path("threads/<int:thread_id>/", views.thread_detail),
    path("threads/<int:thread_id>/likes/", views.thread_likes),
    path("threads/<int:thread_id>/comments/", views.comment_list),
    path("comments/<int:comment_id>/", views.comment_detail),
    path("userbooks/", views.add_to_user_books),
    path("userbooks/check/<int:book_id>/", views.check_user_book),
    path("userbooks/<int:book_id>/", views.remove_from_user_books),
    path("my-threads/", views.my_thread_list),
    path('aladin/search/', views.aladin_search),
]