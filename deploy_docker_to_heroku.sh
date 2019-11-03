#!/bin/bash
app_name=$1
heroku container:login
heroku container:push web -a ${app_name}
heroku container:release web -a ${app_name}
