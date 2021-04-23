# booklibrary

## 📖 Installation
booklibrary can be installed via Pip, Pipenv, or Docker depending upon your setup. To start, clone the repo to your local computer and change into the proper directory.

```
$ git clone https://github.com/bazoor0/booklibrary.git
$ cd booklibrary
```

### Pip

```
$ python3 -m venv booklibrary
$ source booklibrary/bin/activate
(booklibrary) $ pip install -r requirements.txt
(booklibrary) $ python manage.py migrate
(booklibrary) $ python manage.py createsuperuser
(booklibrary) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000/api/book/author/
```

### Pipenv

```
$ pipenv install
$ pipenv shell
(booklibrary) $ python manage.py migrate
(booklibrary) $ python manage.py createsuperuser
(booklibrary) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000/api/book/author/
```

### Docker

```
$ docker build .
$ docker-compose up -d
$ docker-compose run --rm app sh -c "python manage.py migrate"
$ docker-compose run --rm app sh -c "python manage.py createsuperuser"
# Load the site at http://127.0.0.1:8000/api/book/author/
```
