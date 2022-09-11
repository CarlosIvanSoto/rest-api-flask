FROM python:3.11-rc-alpine

WORKDIR /code

ENV FLASK_APP app.py

ENV FLASK_RUN_HOST 0.0.0.0

RUN apk add --no-cache build-base libpq-dev gcc musl-dev linux-headers

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run"]