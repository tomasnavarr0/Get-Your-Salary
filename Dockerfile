FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN pipenv install --system --deploy

COPY . /app

EXPOSE 8000 8501