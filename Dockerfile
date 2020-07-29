FROM python:alpine

COPY src/ /app
WORKDIR /app
RUN apk update
RUN apk add py-pip
RUN apk add py3-setuptools
RUN apk add python3-dev
RUN pip3 install --upgrade pip setuptools
RUN pip3 install -r requirements.txt
ENTRYPOINT flask run --host=0.0.0.0 -p 5000
ENV PORTDOCKER=5000
ENV FLASK_ENV=production
ENV FLASK_APP=app.py
EXPOSE 5000