from rest_framework import serializers
from .models import MyUser , Two_fac


class Two_fac_serializer(serializers.Serializer):
    class Meta:
        model=Two_fac
        fields=('__all__')


class MyUser_serializer(serializers.Serializer):
    class Meta:
        model=MyUser
        fields=('__all__')