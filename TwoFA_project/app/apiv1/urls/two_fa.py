from django.urls import path
from ..views.two_fac import send_otp


urlpatterns = [
    path('two_fac/', send_otp.as_view()),

]
