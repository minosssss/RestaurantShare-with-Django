from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100)


class Restaurant(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_DEFAULT, default=3)
    restaurant_name = models.CharField(max_length=100)  # 맛집 이름
    restaurant_link = models.CharField(max_length=500)  # 맛집 URL
    restaurant_content = models.TextField()  # 맛집설명
    restaurant_keyword = models.CharField(max_length=50)  # 키워드
