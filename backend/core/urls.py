"""
Модуль определяет URL-адреса для тестового задания , используя Django REST framework и drf-yasg
для создания документации API.

Подключаемые модули:
    rest_framework.permissions: Импортирует разрешения Django REST framework.
    drf_yasg.views.get_schema_view: Импортирует функцию для получения представления схемы API.
    drf_yasg.openapi: Импортирует модуль openapi из drf-yasg для определения информации о API.


Маршруты:
    /admin/: Предоставляет доступ к административной панели Django.
    /swagger/: Предоставляет интерфейс Swagger для документации API.
    /api/: Включает маршруты из приложения user_selection.

"""

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.urls import path, include

# pylint: disable=C0103
schema_view = get_schema_view(
   openapi.Info(
      title="Тестовое задание",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include('user_selection.urls')),
]
