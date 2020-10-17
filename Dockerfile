FROM python:3.8.5

RUN	apt update -y
WORKDIR	/app
COPY ./ /app
RUN	pip install -r requirements.txt
ENV	PYTHONUNBUFFERED=1
ENV	TZ=Asia/Seoul