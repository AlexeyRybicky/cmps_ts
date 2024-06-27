"""В модуле содержаться маршруты для приложения `user_selection`"""

from django.urls import path
from .views import UserDetailView

app_name = 'user_selection'

urlpatterns = [
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
]
