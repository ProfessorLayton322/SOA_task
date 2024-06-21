FROM python:3.10

WORKDIR /main

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Setting default host and port. It will probably be overwritten in docker-compose
ENV APP_PORT=32406

ENTRYPOINT python3 main.py
