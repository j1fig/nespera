FROM python:2.7

## Upgrade PIP (and six)
RUN pip install --no-cache-dir --upgrade pip

WORKDIR /app

ADD . /app

# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

ENV NESPERA_DB_URL "/app/db/nespera.sqlite"


CMD ["python", "nespera/parse.py"]
