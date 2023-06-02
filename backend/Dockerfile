FROM python:3.7-slim

RUN mkdir /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY . /app

WORKDIR /app

CMD python manage.py loaddata ingredients.json && python3 manage.py migrate && gunicorn foodgram.wsgi:application --bind 0:8000 