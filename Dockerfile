FROM python:3.10.8-slim

EXPOSE 8000

RUN apt update
RUN apt upgrade -y

RUN mkdir /challenge-api
COPY . /challenge-api
WORKDIR /challenge-api

RUN pip install -r requirements.txt

ENTRYPOINT ["gunicorn"]

CMD ["-c", "python:config.gunicorn", "api.app:create_app()"]
