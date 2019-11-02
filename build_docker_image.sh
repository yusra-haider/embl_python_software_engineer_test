#!/bin/bash
app="python-app"
docker build -t ${app} .
docker run -d -p 80:80 \
  --name=${app} \
  ${app}
#running the tests
docker exec -it ${app} python app/tests.py
if [ $? -ne 0 ]
then
    echo "Tests failed"
    echo "Stopping and removing container"
    docker stop ${app}
    docker rm ${app}
    exit 1
fi