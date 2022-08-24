FROM python:3.10.6-buster

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src ./src

WORKDIR src

CMD ["uvicorn", "--host", "0.0.0.0", "main:app"]
