# 使用官方 Python 3.9 镜像作为基础镜像
FROM python:3.8


WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

