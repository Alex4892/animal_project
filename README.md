
# Сайт животного уголка

Это сайт о животных. Здесь можно разместить объявление о пропаже, находке, а также пристроить животное.

На сайте есть несколько интерфейсов. 

Первый состоит из трёх шагов — регистрация, аутентификация и авторизация — в совокупности часто называются **управлением доступом** или **управлением идентификацией и доступом**.
Это общая система процессов и механизмов, которая обеспечивает правильное управление пользователями и контролирует их доступ к ресурсам в системе.

Второй интерфейс — это публичная часть, где можно подать объявление в зависимости от самой цели, которую преследует посетитель сайта.

Третий интерфейс предназначен для просмотра объявления, а также его изменения и удаления со стороны того пользователя, который ранее создал объявление. 

Четвёртый интерфейс — это панель администратора. Преимущественно им пользуются программисты при разработке сайта. В панели администратор может проставить статус объявления или комментарий пользователя.

Пятый интерфейс предназначен для просмотра избранных объявлений, которых пользователь в процесс посещения "лайкнул". Это некая напоминалка для него о том, что ему мог понравиться интересный материал, и чтобы он в дальнейшем мог его вспомнить.

Шестой интерфейс состоит из фильтрации поиска слов по цели объявления или вида животного. 


## Как запустить dev-версию сайта

Для запуска сайта нужно запустить **одновременно** бэкенд и фронтенд, в двух терминалах.

### Как собрать бэкенд

Скачайте код:

```sh
git clone https://github.com/Alex4892/animal_project.git 
```

Перейдите в каталог проекта:

```sh
cd animal_project
```

[Установите Python](https://www.python.org/), если этого ещё не сделали.

Проверьте, что `python` установлен и корректно настроен. Запустите его в командной строке:

```sh
python --version
```
**Важно!** Версия Python должна быть не ниже 3.9.

Возможно, вместо команды `python` здесь и в остальных инструкциях этого README придётся использовать `python3`. Зависит это от операционной системы и от того, установлен ли у вас Python старой второй версии. 

В каталоге проекта создайте виртуальное окружение:

```sh
python -m venv venv
```
Активируйте его. На разных операционных системах это делается разными командами:

- Windows: `.\venv\Scripts\activate`
- MacOS/Linux: `source venv/bin/activate`


Установите зависимости в виртуальное окружение:

```sh
pip install -r requirements.txt
```

Создать базу данных ```PostgreSQL```. Можно сделать [по этому гайду -](https://www.8host.com/blog/kak-ispolzovat-postgresql-v-prilozhenii-django/) https://www.8host.com/blog/kak-ispolzovat-postgresql-v-prilozhenii-django/

Настроить бэкенд: создать файл `.env` в каталоге `star_burger/` со следующими настройками:

- `DEBUG` — дебаг-режим. Поставьте `False`.
- `SECRET_KEY` — секретный ключ проекта. Он отвечает за шифрование на сайте. Например, им зашифрованы все пароли на вашем сайте.
- `ALLOWED_HOSTS` — [см. документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)
- `DB_URL` - в проекте используется [`dj_database_url`](https://pypi.org/project/dj-database-url/). Добавьте в ```.env``` файл строку вида ```postgres://user:p%23ssword@localhost/dbname```.

Примените миграции командами:

```sh
python manage.py migrate
```

Запустите сервер:

```sh
python manage.py runserver
```

Откройте сайт в браузере по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/).


## Цели проекта

Код написан в учебных целях по проекту о животном уголке
