FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

COPY web/requirements.txt .

RUN python -m pip install --no-cache-dir --upgrade pip setuptools msgpack urllib3 \
    && pip install --no-cache-dir -r requirements.txt
COPY web/ .

EXPOSE 5000

CMD ["python", "app.py"]FROM python:3.12-slim
WORKDIR /app
COPY web/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY web/ .
EXPOSE 5000
CMD ["python", "app.py"]
