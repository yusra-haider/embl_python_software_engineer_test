## EMBL Python Software Engineer Test

This app was developed using FastAPI as the web framework and SQLAlchemy as the means of connection
with the given database.

This app is deployed to Heroku as a docker container. [This](https://yusrapythonapp.herokuapp.com/) 
is the main link for the app, and the documentation is available [here](https://yusrapythonapp.herokuapp.com/docs)

The endpoint is `GET gene_search?name=<name>&species=<species>&limit=<result limit>`, and a sample usage is
[here](https://yusrapythonapp.herokuapp.com/gene_search/?name=abc&species=amphilophus_citrinellus&limit=40)

There are three bash scripts in the repository for ease of testing, building and deploying the
docker container

1. `build_docker_image.sh`: This script builds the docker image, runs the docker container and 
runs tests inside docker (if the argument `yes` is given). Use this script for locally testing and 
running the docker container. Sample usage (testing enabled): `./build_docker_image yes` Run the 
script without arguments for building and running without tests. If the script is run with testing
enabled and the tests failed, the docker container is stopped and the container removed. After this
script is run, the app can be accessed via `localhost:80`


2. `deploy_docker_to_heroku.sh`: This script is for deploying to Heroku with docker. It takes the name
of the deployment target heroku app as an argument. Sample usage: `./deploy_docker_to_heroku.sh <heroku_app_name>`
The script will fail if the heroku app name is not given.

3. `build_test_deploy_docker_to_heroku.sh`: This script combines both the above scripts. It executes 
`build_docker_image.sh` followed by `deploy_docker_to_heroku.sh`. It takes testing enabled / disabled 
as first argument and the heroku app name as the second one. Sample usages: 
`build_test_deploy_docker_to_heroku.sh yes <heroku_app_name>` (testing enabled) and 
`build_test_deploy_docker_to_heroku.sh no <heroku_app_name>` (without testing)

The repository is currently connected to Travis CI, and has the CI / CD pipeline in place. Tests are executed and if successful, the app is deployed to Heroku as a docker container. Currently, builds get executed on every pushed change and on every pull request.
 
Experimenting a CI/CD set up with GitHub actions is in progress on [this](https://github.com/yusra-haider/embl_python_software_engineer_test/tree/setting_up_github_actions)
branch

##### Instructions for running the app inside vagrant, using [this](https://github.com/joanmarcriera/vagrant-file) vagrant file:

```
$ git clone https://github.com/yusra-haider/embl_python_software_engineer_test.git
$ cd embl_python_software_engineer_test.git
$ ./build_docker_image yes
```

This should get the docker container up and running inside vagrant. Access the app via `localhost:8080`, and the documentation
via `localhost:8080/docs`
A sample usage of the endpoint would look like 
`http://localhost:8080/gene_search/?name=abc&species=amphilophus_citrinellus`


