#!/bin/bash
run_tests=$1
heroku_app_name=$2

./build_docker_image.sh $1
if [ $? -eq 0 ]
then
    ./deploy_docker_to_heroku.sh ${heroku_app_name}
else
    echo "docker build/ test failed"
fi