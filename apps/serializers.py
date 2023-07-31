from rest_framework import serializers

from apps.models import Publisher


# 序列化接口，只有这里返回view才能看到
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'age']
