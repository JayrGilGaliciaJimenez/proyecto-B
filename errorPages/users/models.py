from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.db import models
from django.utils.timezone import now
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, name, surname, age, tel, control_number, **extra_fields):
        if not email:
            raise ValueError('El correo electrónico es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.name = name
        user.surname = surname
        user.age = age
        user.tel = tel
        user.control_number = control_number
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    control_number = models.CharField(max_length=10)
    age = models.IntegerField()
    tel = models.CharField(max_length=10)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=now)
    
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname', 'control_number', 'age', 'tel']

    def __str__(self):
        return self.email
