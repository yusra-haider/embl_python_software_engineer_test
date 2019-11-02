# get the base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-alpine3.8
# set work directory
WORKDIR /app
# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# copy project
COPY . .


