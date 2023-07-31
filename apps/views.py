from django.shortcuts import render
from apps import models
from rest_framework import viewsets

from apps.serializers import UserSerializer


# Create your views here.
# def publisher_list(request):
#     obj = models.Publisher.objects.all()  # 获取所有对象
#     print(11, obj.values())
#     return render(request, 'publisher_list.html', {'publisher_list': obj})  # {'publisher_list': obj}是模板，可以传递给前端页面。

# 视图返回接口
class UserViewSet(viewsets.ModelViewSet):
    queryset = models.Publisher.objects.all()
    serializer_class = UserSerializer
