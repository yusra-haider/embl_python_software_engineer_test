#!/bin/bash
app="python-app"
run_tests=$1
docker build -t ${app} .
docker run -d -p 80:80 \
  --name=${app} \
  ${app}

#running the tests
if [ "$run_tests" == "yes" ]
then
    echo "gotta run them tests"
    # I can run the tests inside the docker container
    # or I can run the python scripts externally
    # I think it's perhaps more appropriate to set up a separate test
    # container altogether.. This is something worth going over in the code review
    docker exec -it ${app} python app/tests.py
    #python app/tests.py
    if [ $? -ne 0 ]
    then
        echo "Tests failed"
        echo "Stopping and removing container"
        docker stop ${app}
        docker rm ${app}
        exit 1
    fi
fi
