FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-alpine3.8
COPY ./requirements.txt /var/app/requirements.txt
RUN pip install -r  /var/app/requirements.txt
COPY ./app /app

