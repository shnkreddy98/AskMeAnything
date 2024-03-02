FROM python:3.9

RUN pip install -r requirements.txt


WORKDIR /app

COPY audiofiles .
COPY *.py .
COPY REQUIREMENTS.txt .

ENTRYPOINT [ "python3", "main.py"]