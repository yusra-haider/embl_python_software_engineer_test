#!/bin/bash
heroku_app_name=$1
./build_docker_image.sh
if [ $? -eq 0 ]
then
    ./deploy_docker_to_heroku.sh ${heroku_app_name}
else
    echo "docker build/ test failed"
fi