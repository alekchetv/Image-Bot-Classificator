FROM python:3.12.4-slim

ADD bot.py /bot/
ADD messages.py /bot/
ADD requirements.txt /bot/
ADD config.py /bot/

WORKDIR /bot/

RUN pip install -r requirements.txt