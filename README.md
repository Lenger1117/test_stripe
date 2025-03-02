# Опиcание проекта
Это простой сервер с простеньким html, который общается со Stripe и создает платёжные формы для товаров.

# Стек проекта:
- Python
- Django
- Docker

# Проект доступен по ссылкам:
```
http://test-stripe.zapto.org/admin
```
```
http://test-stripe.zapto.org/item/1
```


# Данные для проверки работы приложения (суперюзер):
```
- username: admin
- password: admin
```




# Инструкции по установке локально:
### 1. Клонируйте проект:
```
git clone https://github.com/Lenger1117/foodgram-project-react.git
```
### 2. Установите и активируйте виртуальное окружение:
```
python3 -m venv venv или python -m venv venv
```
```
source venv/bin/activate или source venv/Scripts/activate
```
### 3. Установите зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
### 4. В папке с файлом manage.py примените миграции:
```
python manage.py migrate
```
### 5. Создайте суперюзера:
```
python manage.py createsuperuser
```
### 6. В папке с файлом manage.py выполните команду для запуска локально:
```
python manage.py runserver
```

