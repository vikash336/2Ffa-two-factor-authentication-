FROM python:3.8
ENV APP_HOME /app
WORKDIR ${APP_HOME}
COPY requirements.txt ./app/requirements.txt
COPY . .
RUN pip install --upgrade pip
ENV PORT 8000
ENV PYTHONUNBUFFERED=True
RUN pip install -r ./app/requirements.txt
COPY . /app/

CMD python manage.py runserver 0.0.0.0:8000