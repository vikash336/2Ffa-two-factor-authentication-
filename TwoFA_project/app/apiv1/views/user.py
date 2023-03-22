from ...models import UserAccount, TwoFaToken
from ...serializers import MyUser_serializer, Two_fac_serializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
import json
from django.core.mail import send_mail
import random as r
from django.utils.crypto import get_random_string
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_200_OK
class send_otp(APIView):

    def post(self, request):
        email=request.data['email']
        password=request.data['password']

        verify_email=UserAccount.objects.filter(email=email).first()
        if verify_email is None:
            raise AuthenticationFailed({
                "Status": "Email Not Registered"
            })

        if verify_email.check_password(password) is False:
            raise AuthenticationFailed({
                "Status": "Incorrect Password"
            })
        user_tokens = TwoFaToken.objects.filter(user=verify_email)
        if user_tokens.exists():
            user_tokens.delete()
        token = TwoFaToken.objects.create(user=verify_email,
                                          token=get_random_string(
                                              length=6,
                                              allowed_chars="0123456789"))

        subject = 'OTP for 2FA'
        message = token.token
        from_email = 'vikashgusain1999@gmail.com'
        recipient_list = ['vikash.gusain@bonamisoftware.com',]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)


        return Response({
            'detail':'2fa code has been sent to your inbox'
            },status=HTTP_200_OK)

class VerifyTwoFactorAPIView(APIView):
    def post(self, request):
        email=request.data['email']
        otp=request.data['otp']

        print("******")
        verify_email=UserAccount.objects.filter(email=email).first()
        # user_token=TwoFaToken.objects.get(user=user,token=data['token'])
        user_token = get_object_or_404(TwoFaToken,
                                       user=verify_email,
                                       token=otp)
        print(user_token)
        user_token.delete()
        return Response({
            'detail':'Accepted'

        },status=HTTP_200_OK)