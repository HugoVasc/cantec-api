FROM python:3.10-slim


ENV PYTHONUNBUFFERED True


ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000/tcp

# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 -k uvicorn.workers.UvicornWorker main:app

CMD ["python", "main.py"]

# CMD ["gunicorn" "main:app" "-w 4" "-k uvicorn.workers.UvicornWorker"]