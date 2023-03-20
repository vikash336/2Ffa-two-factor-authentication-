from django.contrib import admin
from .models import UserAccount, TwoFaToken


admin.site.register(UserAccount)
admin.site.register(TwoFaToken)
