# issue/python/Dockerfile

FROM	python:latest

RUN	apt update -y && apt install -y cron vim
WORKDIR	/app
COPY	requirements.txt /app
RUN	pip install -r requirements.txt
ENV	PYTHONUNBUFFERED=1
ENV	TZ=Asia/Seoul
