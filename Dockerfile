FROM python:3.8.5-slim

RUN	apt update -y && apt install -y libpq-dev gcc
WORKDIR	/app
COPY ./ /app
RUN	pip install -r requirements.txt
ENV	PYTHONUNBUFFERED=1
ENV	TZ=Asia/Seoul

