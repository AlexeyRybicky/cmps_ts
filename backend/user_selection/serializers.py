"""Модуль сериализаторов для приложения `user_selection`"""

from rest_framework import serializers
from django.apps import apps


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели пользователя"""

    # pylint: disable=missing-docstring
    class Meta:
        model = apps.get_model('user_selection', 'User')
        fields = ['id', 'username', 'role', 'offer', 'avatar']
