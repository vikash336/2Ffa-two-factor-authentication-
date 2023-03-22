from rest_framework import serializers
from ...models import UserAccount , TwoFaToken


class Two_fac_serializer(serializers.Serializer):
    user=serializers.CharField(max_length=100)
    class Meta:
        model=TwoFaToken
        fields=('__all__')


class MyUser_serializer(serializers.Serializer):
    class Meta:
        model=UserAccount
        fields=('__all__')