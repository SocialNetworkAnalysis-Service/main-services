FROM python:3.9-slim

RUN apt-get update

COPY services/admin_panel /admin_panel/
WORKDIR /admin_panel

RUN apt-get install -y gcc

# Ставим модули
RUN pip3 install -r requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/admin_panel/"

# Наконец, запускаем сервер
CMD ["gunicorn", "main:app", "--bind=0.0.0.0:777", "--reload"]