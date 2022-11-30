FROM python:3.10

RUN mkdir /app
WORKDIR /app

COPY ./utils /app/utils
COPY model/data /app/data
COPY model/model.py /app/model.py
COPY cleaning_for_model/requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "model.py"]