FROM python:3.12-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# Установка Python-зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта
COPY . .

# Открываем порт (если используешь, например, gunicorn)
EXPOSE 8000

# Старт команды (можно заменить, если используешь другой сервер)
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
