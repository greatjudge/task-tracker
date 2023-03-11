# базовый образ
FROM python:3

# Создаем папку task_tracker и устнавливаем рабочий каталог контейнера
WORKDIR /task_tracker

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /task_tracker
# Устанавливаем библиотеки из requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем все файлы из локального проекта в контейнер
ADD . /

# Указывем, какой порт будет прослушивать контейнер
EXPOSE 8000

RUN chmod +x /backend-entrypoint.sh
#ENTRYPOINT '../backend-entrypoint.sh'
