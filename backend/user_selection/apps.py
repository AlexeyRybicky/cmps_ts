"""В модуле содержаться настройки приложения"""

from django.apps import AppConfig


class UserSelectionConfig(AppConfig):
    """Настройки `user_selection` приложения"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_selection'
