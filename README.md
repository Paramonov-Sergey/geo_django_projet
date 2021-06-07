## Инструменты разработки
## Стек:
    Python >= 3.8
    Django 
    SqlLite
    geopy
    geoip
# Старт
#### 1) Сделать форк репозитория
### 2) Клонировать репозиторий
    git clone ссылка_сгенерированная_в_вашем_репозитории
### 3) Создать виртуальное окружение
    python -m venv имя_окружения
### 4) Установить все зависимости
    pip install -r requerements.txt
### 5) Сделать миграции
    python manage.py makemigrations
    python manage.py migrate
### 6) Создать суперюзера
     python manage.py createsuperuser
### 7) Перейти по адресу
    http://127.0.0.1:8000/
