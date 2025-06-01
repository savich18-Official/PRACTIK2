# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости через Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN /root/.local/bin/poetry install --no-dev

# Открываем порт для приложения
EXPOSE 8000

# Запускаем приложение
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
