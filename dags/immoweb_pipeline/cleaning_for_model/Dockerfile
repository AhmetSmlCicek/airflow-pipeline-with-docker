FROM python:3.10

RUN mkdir /app
WORKDIR /app

COPY ./utils /app/utils
COPY cleaning_for_model/data /app/data
COPY cleaning_for_model/preprocessing.py /app/preprocessing.py
COPY cleaning_for_model/requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "preprocessing.py"]