"""В модуле содержаться представления для `user_selection` приложения"""

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer


class UserDetailView(APIView):
    """
    Класс представления для получения информации о пользователе

    Атрибуты:
        pk: Целочисленный идентификатор пользователя.

    Методы:
        get: Получает информацию о пользователе с заданным идентификатором.
    """

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
