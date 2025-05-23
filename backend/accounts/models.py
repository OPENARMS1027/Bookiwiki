from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from books.models import Category, Book

class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', '남성'),
        ('F', '여성'),
    )
    username = models.CharField(max_length=100, unique=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        null=True,
    )
    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    interested_category = models.ManyToManyField(
        Category,
        blank=True,
        related_name="users",
    )
    week_avg_time = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    year_avg_time = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    profile_img = models.ImageField(
        upload_to='user_profile_img/',
        blank=True,
        null=True,
    )
    followings = models.ManyToManyField(
        'self', symmetrical=False, related_name='followers'
    )
    books = models.ManyToManyField(
        Book, related_name='likes_users'
    )