from django.db import models

# Create your models here.

# PK
class bookcode(models.Model):
    booktitle = models.CharField(max_length=200)
    yes24_code = models.CharField(max_length=50)

# 도서별 데이터
class bookdata(models.Model):
    bookcode = models.ForeignKey(bookcode, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    published_date = models.CharField(max_length=50)

# 일별 데이터
class bookrank(models.Model):
    bookcode = models.ForeignKey(bookcode, on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)
    
    