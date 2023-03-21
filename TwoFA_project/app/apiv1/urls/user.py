from django.contrib import admin
from django.urls import path, include
from ..views.user import send_otp


urlpatterns = [
    path('Login/', send_otp.as_view()),

]
