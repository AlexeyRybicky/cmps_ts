"""В модуле содержаться классы для работы с админ панелью"""

from django.contrib import admin
from user_selection.models import User

# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Класс представляет административную панелья для управления пользователями"""
    list_display = (
        'id',
        'username',
    )
    fields = (
        'username',
        'email',
        'role',
        'offer',
        'avatar',
        'password',
        'is_superuser'
    )
    list_display_links = (
        'id',
        'username'
    )
