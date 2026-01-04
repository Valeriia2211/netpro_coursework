FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install flask flask-httpauth pytest

EXPOSE 8001

CMD ["python", "app/rest_api.py"]
