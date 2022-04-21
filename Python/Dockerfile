# syntax=docker/dockerfile:1

FROM python:3.10.4-bullseye

WORKDIR /app

COPY /requirements/requirements.txt /app/requirements/requirements.txt
RUN pip install -r /app/requirements/requirements.txt

COPY . .

CMD [ "uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080", "--reload"]
 