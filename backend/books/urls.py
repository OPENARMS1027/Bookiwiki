from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.book_list),
    path("categories/", views.category_list),
]
