from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('이메일은 필수입니다.')
        user = self.model(
            email = email
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, email=None, password=None):
        superuser = self.create_user(
            email = email,
            password = password,
        )
        superuser.is_superuser = True
        superuser.is_staff = True
        superuser.is_activate = True
        superuser.save(using=self.db)
        return superuser

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'

