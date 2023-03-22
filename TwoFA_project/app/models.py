from django.db import models

from django.contrib.auth.models import AbstractBaseUser, UserManager, AbstractUser

class UserAccountManager(UserManager):
    def get_by_natural_key(self, username):
        return self.get(
            models.Q(**{self.model.USERNAME_FIELD: username})
            | models.Q(**{self.model.EMAIL_FIELD: username}))
    def create_user(self, email=None, password=None, **extra_fields):
        return super().create_user(username=extra_fields.get('phone'),
                                   email=email,
                                   password=password,
                                   **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        return super().create_superuser(username=extra_fields.get('phone'),
                                        email=email,
                                        password=password,
                                        **extra_fields)

class UserAccount(AbstractUser):
    country=models.CharField(max_length=128,default="India")
    phone=models.IntegerField(unique=True)
    email=models.EmailField(unique=True)
    is_staff=models.BooleanField(default=False)
    # is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[
        'phone'
    ]

    objects = UserAccountManager()

    def __str__(self):
        return self.email

class TwoFaToken(models.Model):
    user = models.ForeignKey(UserAccount,
                             related_name='two_fa_tokens',
                             on_delete=models.CASCADE)
    token = models.CharField(max_length=15)



    def __str__(self):
        return f'{self.user}'