# Блогикум

Один из учебных проектов, текущий пет-проект - ingridients_collector https://github.com/Exert1/ingridients_collector

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Exert1/Blogicum.git
```

```
cd Blogicum
```

Cоздать и активировать виртуальное окружение:

```
py -3.9 -m venv venv
```

```
source venv/Scripts/activate
```

```
py -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Перейти в директорию с менеджером:
```
cd blogicum
```

Выполнить миграции:

```
py manage.py migrate
```

Запустить проект:

```
py manage.py runserver
```
