FROM python:3.10

RUN mkdir /app
WORKDIR /app

COPY ./utils /app/utils
COPY cleaning_for_analysis/data /app/data
COPY cleaning_for_analysis/cleaning.py /app/cleaning.py
COPY cleaning_for_analysis/requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "cleaning.py"]