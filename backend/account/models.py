from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.models import BooleanField

from project.managers import UserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=120, unique=True)
    full_name = models.CharField(max_length=120, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None) -> BooleanField:
        return self.is_admin

    def has_module_perms(self, app_label) -> BooleanField:
        return self.is_admin

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
