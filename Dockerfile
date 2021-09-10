FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .

RUN apt update && apt install -y \
    gcc \
    g++ \
    git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt --no-cache-dir

CMD [ "python", "./src/main.py" ]