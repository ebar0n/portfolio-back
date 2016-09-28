# Portfolio API

[![Build Status](https://travis-ci.org/ebar0n/portfolio-back.svg?branch=master)](https://travis-ci.org/ebar0n/portfolio-back)

## Requirements

### Install and configure Docker

* Install docker. [Docker](https://www.docker.com)

* Intall docker-compose. [Compose](https://docs.docker.com/compose/install/)

### Set Var Environment

* Copy to `env.example` into `.env`

```sh
cp env.example .env
```

* Edit values in `.env`

```sh
nano .env
```

* Config domain

```sh
echo "127.0.0.1 dev.portfolio.com" | sudo tee -a /etc/hosts > /dev/null
echo "127.0.0.1 dev.api.portfolio.com" | sudo tee -a /etc/hosts > /dev/null
```

### Enable cache for Dev

* Install

```sh
docker pull ebar0n/proxy-cache
docker run --name proxy-cache -d --restart=always \
--publish 3128:3128 --publish 3141:3141 --publish 3142:3142 \
--volume ~/data/proxy-cache/squid/:/var/spool/squid3 \
--volume ~/data/proxy-cache/devpi:/var/.devpi/server \
--volume ~/data/proxy-cache/aptcacherng:/var/cache/apt-cacher-ng \
ebar0n/proxy-cache
```

* Using

```sh
docker start proxy-cache
```


* Check cache container IP == "172.17.0.2"

```sh
docker inspect proxy-cache | grep '"IPAddress":'
```

* Build containers

```sh
docker-compose build
```

## BackEnd

* Start container DB

```sh
docker-compose up -d postgres
```

* Apply migrations

```sh
docker-compose run --rm api python manage.py migrate
```

* Run Django Project

```sh
docker-compose up -d
```

* Open project on browser [dev.portfolio.com](http://dev.portfolio.com)

* Open API on browser [dev.api.portfolio.com](http://dev.api.portfolio.com)

* Open API on browser optional in Dev [dev.api.portfolio.com:8000](http://dev.api.portfolio.com:8000)

### Django Admin

* Create superuser (Execute command and follow the steps)

```sh
docker-compose run --rm api python manage.py createsuperuser
```

* Access to django admin [dev.api.portfolio.com/admin/](http://dev.api.portfolio.com/admin/)

### Run tests to code

* Exit instantly on first error or failed test

```sh
docker-compose run --rm api py.test -x
```

* Activate the Python Debugger

```sh
docker-compose run --rm api py.test --pdb
```

* Run all the tests

```sh
docker-compose run --rm api py.test
```

### Run tests to style

* Run tests isort

```sh
docker-compose run --rm api isort -c -rc -df
```

* Run tests flake8

```sh
docker-compose run --rm api flake8
```

### Django Internationalization

* Execute this command to runs over the entire source tree of the current directory and pulls out all strings marked for translation.

```sh
docker-compose run --rm api python manage.py makemessages -l es
```

* Edit file api/locale/es/LC_MESSAGES/api.po and add a translation.

```sh
#: module/file.py:12
msgid "Hello world"
msgstr "Hola mundo"
```

* Compiles .po files to .mo files for use with builtin gettext support.

```sh
docker-compose run --rm api python manage.py compilemessages
```

### Run the project for Production

* Build

```sh
docker-compose -f docker-compose-production.yml build
```

* Initialize

```sh
docker-compose -f docker-compose-production.yml up -d postgres
docker-compose -f docker-compose-production.yml run --rm api python manage.py migrate --noinput
docker-compose -f docker-compose-production.yml run --rm api python manage.py collectstatic --noinput
docker-compose -f docker-compose-production.yml run --rm api python manage.py compilemessages
```

* Run Django server

```sh
docker-compose -f docker-compose-production.yml up -d
```

* Visit [dev.portfolio.com](https://dev.portfolio.com/)

### Automatic deploy using `fabric`

```sh
pip install fabric
~/.local/bin/fab deploy
```

* fab log
* fab pull
* fab build
* fab test
