from django.urls import path
from . import views

urlpatterns = [
    path("<int:user_id>/", views.user_info),
    path("me/", views.this_user),
    path("follow/<int:user_id>/", views.user_follow),
]
