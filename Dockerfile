FROM python:3.11-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app

COPY data/model_training/rfc.pkl /app/data/model_training/rfc.pkl

RUN pip install -r requirement.txt

CMD ["python3", "app.py"]