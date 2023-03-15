FROM PYTHON3.9

ENV PYTHONUNBUFFERED 1

WORKDIR  /app

COPY requirements.txt ./app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app/

RUN python manage.py runserver 0.0.0.0:8000
