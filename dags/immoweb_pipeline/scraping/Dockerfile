FROM python:3.10

RUN mkdir /app
WORKDIR /app

COPY ./utils /app/utils

COPY scraping/driver /app/driver
COPY scraping/data /app/data
COPY scraping/scraping.py /app
COPY scraping/requirements.txt /app

RUN apt update -y
RUN apt install firefox-esr -y
RUN pip install -r requirements.txt

CMD ["python", "scraping.py"]