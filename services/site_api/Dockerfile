FROM python:3.9-slim

RUN apt-get update

COPY services/site_api /site_api/
WORKDIR /site_api

RUN apt-get install -y gcc

# Ставим модули
RUN pip3 install -r requirements.txt


ENV PYTHONPATH="${PYTHONPATH}:/site_api/"