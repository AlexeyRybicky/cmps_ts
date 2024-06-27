"""В модуле содержится команда Django для создания начальных пользователей с различными ролями."""

import uuid

from django.core.management.base import BaseCommand

from user_selection.models import User


class Command(BaseCommand):
    """Создает пользователей с уникальными именами, ролями и аватарами на основе доступных значений."""
    def handle(self, *args, **options):
        roles = User.Role.choices
        avatars = ['user.png', 'manager.png', 'crm_admin.png']
        for i, (role_value, role_name) in enumerate(roles):
            unique_suffix = str(uuid.uuid4())[:3]
            user = User.objects.create(
                username=f'{role_name}_{unique_suffix}',
                email=f'{role_name}_{unique_suffix}@mail.com',
                role=role_value,
                avatar=f'avatars/{avatars[i]}'
            )
            self.stdout.write(f'Пользователь {user.username} успешно создан')
