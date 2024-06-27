"""В модуле содержаться модели для базы данных приложения `user_selection`."""

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from user_selection.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Класс User представляет модель пользователя с расширенными возможностями для
    управления пользователями в приложении.
    """
    objects: models.Manager = UserManager()

    class Role(models.TextChoices):
        USER = "user", _("Пользователь")
        MANAGER = "manager", _("Менеджер")
        CRM_ADMIN = "crm_admin", _("CRM-администратор")

    username = models.CharField(
        max_length=255,
        unique=True,
        help_text='Имя пользователя'
    )
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER,
        help_text='Поле для определения роли пользователя. '
    )
    offer = models.BooleanField(
        default=False,
        help_text='Поле для обозначения наличия предложения для пользователя'
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        default='default_avatar.png',
        help_text='Аватар пользователя'
    )
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
