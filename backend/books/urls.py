from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.book_list),
    path("books/<int:book_id>/", views.book_detail),
    path("categories/", views.category_list),
    path("threads/", views.thread_list),
    path("threads/<int:thread_id>/", views.thread_detail),
]
