# Read_me

1. Скачать репозиторий
```shell
git clone <ссылка на репозиторий>
```
2. Перейти в каталог cmps_ts
3. Создайте .env файл (за образец используйте .env.template)
3. Для запуска проекта выполнить команду
```shell
docker compose -f docker-compose.yml up --build
```
4. Войти в контейнер с приложением выполнив команду:
```shell
docker exec -it cmps_ts-app-1 /bin/bash  
```

5. Внутри контейнера:

   - для создания суперпользователя выполнит команду
    ```shell
    python manage.py createsuperuser
    ```
   - для создания пользователей выполнить команду
    ```shell
    python manage.py create_users
    ```
6. Для дальнейшей работы с созданными пользователями можно перейти в админ панель по адресу http://localhost:8000/admin/
7. Для проверки получения пользователя по id можно воспользоваться swagger по адресу http://localhost:8000/swagger/
