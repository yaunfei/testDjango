from django.db import models


# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=128)  # 出版社名称
    age = models.IntegerField('年龄', null=False)  # 年龄
