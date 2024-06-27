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
    """

    # pylint: disable=W0613
    def get(self, request, pk):
        """Получает информацию о пользователе с заданным идентификатором."""
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
