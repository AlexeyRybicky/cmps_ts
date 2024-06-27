"""
В модуле содержится класс UserManager, представляет менеджер пользователей Django
для создания обычных пользователей и суперпользователей.
"""

from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """Класс создания пользователей"""
    def create_user(self, username, email, password=None):
        """Создает обычного пользователя"""
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        """Создает суперпользователя"""
        user = self.create_user(username, email, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
