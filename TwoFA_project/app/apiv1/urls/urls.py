from django.contrib import admin
from django.urls import path, include
from .views import send_otp


urlpatterns = [
    path('test/', send_otp.as_view()),

]
