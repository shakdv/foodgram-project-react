![Foodgram Workflow Status](https://github.com/shakdv/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg?branch=master&event=push)
# Foodgram — «Продуктовый помощник»

## Описание проекта Foodgram
«Продуктовый помощник»: приложение, в котором пользователи публикуют рецепты, могут подписываться на публикации других авторов и добавлять рецепты в избранное.
Сервис «Список покупок» позволит пользователю создавать список продуктов, которые нужно купить для приготовления выбранных блюд.

Проект развернут по адресу http://foodgram.shakhlin.ru

## Реализовано в CI/CD
* автоматический запуск тестов
* обновление образов на Docker Hub
* автоматический деплой на боевой сервер при пуше в главную ветку (master или main)
* отправка сообщения в Telegram через бота об успешном деплое

## Технологии
* Python 3.7
* Django 3.2.14
* DRF
* Docker
* Docker-Compose
* Nginx
* PostreSQL
* GitHub Actions

## Запуск проекта в dev-режиме

Установить и активировать виртуальное окружение:
```
python -m venv venv
source /venv/bin/activated
```

Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:
```
python manage.py makemigrations

python manage.py migrate
```

В папке с файлом manage.py выполнить команду:
```
python manage.py runserver
```

## Запуск проекта через Docker Compose

Установите docker, docker-compose на сервере:
```
ssh username@ip
```
```
sudo apt update && sudo apt upgrade -y && sudo apt install curl -y
```
```
sudo curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh && sudo rm get-docker.sh
```
```
sudo curl -L "https://github.com/docker/compose/releases/download/v2.9.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
```
sudo chmod +x /usr/local/bin/docker-compose
```

Создайте директорию infra:

```
mkdir infra
```
* Перенести файлы docker-compose.yml и default.conf на сервер директорию infra:

```
scp docker-compose.yml username@server_ip:/home/<username>/infra
```
```
scp default.conf <username>@<server_ip>:/home/<username>/infra
```

Перейдите в каталог:
```bash
cd infra
```

Добавьте файл .env в котором хранится SECRET_KEY и настройки БД:
```bash
echo "SECRET_KEY=YourSecretKey 
DB_ENGINE=django.db.backends.postgresql 
DB_NAME=postgres 
POSTGRES_USER=postgres 
POSTGRES_PASSWORD=postgres 
DB_HOST=db DB_PORT=5432" > .env
```
Пример заполнения файла .env:
```
SECRET_KEY=i8n#^u!c+u95k0b2*uraj)8b00(%p3ip9f*ze7s&+%8$r4bi5m
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql 
DB_NAME=postgres # имя базы данных 
POSTGRES_USER=postgres # логин для подключения к базе данных 
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой) 
DB_HOST=db # название сервиса (контейнера) 
DB_PORT=5432 # порт для подключения к БД
```
В директории infra выполнить команду, чтобы запустить проект:
```
sudo docker-compose up -d
```

Выполнить миграции:
```
sudo docker-compose exec backend python manage.py makemigrations
```
```
sudo docker-compose exec backend python manage.py migrate --noinput
```
Создать суперпользователя:
```
sudo docker-compose exec backend python manage.py createsuperuser
```
Собрать статику:
```
sudo docker-compose exec backend python manage.py collectstatic --no-input
```

Дополнительно можно наполнить базу данных ингредиентами и тегами:
```
sudo docker-compose exec backend python manage.py load_tags
```
```
sudo docker-compose exec backend python manage.py load_ingredients
```

## Запуск проекта через Docker
- В папке infra выполнить команду, чтобы собрать контейнер:

```
sudo docker-compose up -d
```

Для доступа к контейнеру выполните следующие команды:

```
sudo docker-compose exec backend python manage.py makemigrations
```
```
sudo docker-compose exec backend python manage.py migrate --noinput
```
```
sudo docker-compose exec backend python manage.py createsuperuser
```
```
sudo docker-compose exec backend python manage.py collectstatic --no-input
```

Дополнительно можно наполнить базу данных ингредиентами и тэгами:

```
sudo docker-compose exec backend python manage.py load_tags
```
```
sudo docker-compose exec backend python manage.py load_ingredients
```
