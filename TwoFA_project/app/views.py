from django.shortcuts import render
from .models import MyUser , Two_fac
from .serializers import MyUser_serializer, Two_fac_serializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed


class send_otp(APIView):
    pass
