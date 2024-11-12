FROM python:3-alpine

RUN pip3 install flask

COPY . /app/

WORKDIR /app

EXPOSE 5000

ENTRYPOINT [ "flask", "--app","app","run","--host=0.0.0.0"]