# SecondDjango

Учебное веб-приложение в УЦ "Специалист" на Django для отображения сниппетов.

## Возможности SecondDjango

- Добавление сниппета
- Отображение всех сниппетов
- Изменение сниппета
- Удаление сниппета
- Поиск сниппета
- Регистрация новых пользователей и авторизация
- Разграничение прав доступа к изменению сниппета

## Технологии

- python 3.10+ - высокоуровневый язык программирования общего назначения
- django 5.1.1 - фреймворк для веб-приложений на языке Python

## Установка на локальной машине

1. Клонировать репозиторий c GitHub
```
$ git clone https://github.com/Le0har/SecondDjango
```
2. Создать виртуальное окружение
```
$ python3 -m venv django_venv
```
3. Запустить виртуальное окружение
```
$ source django_venv/bin/activate
```
4. Обновить менеджер пакетов pip
```
$ python -m pip install --upgrade pip
```
5. Установить зависимости из ```requirements.txt```
```
$ pip install -r requirements.txt
```

6. Выполнить миграции
```
$ python manage.py migrate
```

7. Записать данные в БД (опционально)
```
$ python manage.py loaddata MainApp/fixtures/save_all.json
```

8. Запустить проект
```
$ python manage.py runserver
```

## Автор

Тихонов Алексей [https://github.com/Le0har](https://github.com/Le0har)
