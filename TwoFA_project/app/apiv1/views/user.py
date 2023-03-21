from django.shortcuts import render
from ...models import UserAccount, TwoFaToken
from ...serializers import MyUser_serializer, Two_fac_serializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
import json
from django.core.mail import send_mail
from django.shortcuts import render


class send_otp(APIView):

    def post(self, requset):
        email=requset.data['email']
        password=requset.data['password']

        verify_email=UserAccount.objects.filter(email=email).first()
        # user_data = authenticate(email=email, password=password)

        if verify_email.check_password(password) is False:
            raise AuthenticationFailed({
                "Status": "Incorrect Password"
            })

        user_tokens = TwoFaToken.objects.filter(user=verify_email).first()
        
        subject = 'Subject of the Email'
        message = 'Body of the Email'
        from_email = 'vikashgusain1999@gmail.com'
        recipient_list = ['vikash.gusain@bonamisoftware.com',]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)



        return Response({
            'detail':'2fa code has been sent to your inbox'
            })
