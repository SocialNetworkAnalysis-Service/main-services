FROM python:3.8-alpine

RUN apk add gcc
RUN apk add nano
RUN apk add g++
RUN apk add musl-dev
COPY . /chat_bot/
WORKDIR /chat_bot
# Ставим модули
RUN pip3 install -r requirements.txt

# Наконец, запускаем сервер 
CMD ["python3", "main.py"]
