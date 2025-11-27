# Taxi Service Project

Django project for managing drivers, cars and manufacturers in Taxi Service

## Check it out

[Taxi Service](http://3.70.245.224:8000/)

## Installation

Python3 must be already installed

## Run with Docker (Recommended)

Docker handles the installation of Python dependencies, Playwright browsers, and the PostgreSQL database automatically.

1. **Clone the repository**
   ```shell
   git clone [https://github.com/oleksandra-halytska/taxi-service](https://github.com/oleksandra-halytska/taxi-service)
   cd taxi-service
   ```

2. **Configure and Run**

   Create a `.env` file with the required variables:
   ```text
   POSTGRES_DB=taxi_db
   POSTGRES_USER=taxi_user
   POSTGRES_PASSWORD=secret
   POSTGRES_HOST=db
   ```
   Execute:
   ```shell
   docker-compose up -d --build
   ```
3. **Open http://127.0.0.1:8000/ in your browser.**

## Manual Installation

```shell
python3 -m venv venv
source venv/bin/activate  # on Mac OS / Linux
# venv\Scripts\activate   # on Windows

pip install -r requirements.txt
playwright install chromium # Required for UI tests
playwright install-deps

python3 manage.py makemigrations
python3 manage.py migrate
python manage.py runserver
```

# Run all tests
```shell
docker compose run --rm web pytest
```

# Run only smoke tests
```shell
docker compose run --rm web pytest -m smoke    
```

## Features

* Authentication functionality for Driver/User
* Managing drivers, cars and manufacturers using crud operations from website
* Powerful admin panel for advanced managing

## Demo

![Website Interface](site.png)

## To check project use next credentials:
* login: test
* password: 123456
