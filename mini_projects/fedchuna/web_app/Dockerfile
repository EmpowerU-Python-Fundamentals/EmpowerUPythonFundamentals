# Dockerfile
FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    gcc \
    libldap2-dev \
    libsasl2-dev \
    netcat-traditional \ 
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

COPY . .


RUN chmod +x wait-for-it.sh

EXPOSE 5001


CMD ["./wait-for-it.sh", "db:5432", "--", "python", "-m", "gunicorn", "--bind", "0.0.0.0:5001", "web_app:app"]