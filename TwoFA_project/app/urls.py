from django.urls import path, include

urlpatterns = [
    path('v1/', include('app.apiv1.urls.user')),
    path('v1/2fa/', include('app.apiv1.urls.two_fa')),
]
