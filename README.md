# Endocode_Challenge

This challenge consists of developing a HTTP service for returning specified strings according to the given HTTP endpoints, testing the service, deploying docker container, creating a CI/CD pipeline and deploying the service on kubernetes. 

## Dependencies

+ Python 
+ Python modules - requests
+ GitHub
+ Docker
+ Kubernetes (minikube and kubectl)

## Level 1

## Usage
Running the command 'curl http://localhost:8080/helloworld' returns "Hello Stranger"

Running the command 'curl http://localhost:8080/helloworld?name=AlfredENeumann' returns "Hello
Alfred E Neumann" (camel-case gets cut by spaces)

Running the command 'curl http://localhost:8080/versionz' returns JSON with Git hash and name of the project.
Note: To access the git hash, personal access token has to be provided. Personal access token will be provided upon request.

## Task file

This is a utility for running the service through zsh terminal

Commands:

To start the server first in zsh terminal:

+ task run_Server

Then to access the endpoints in zsh terminal: 
In the third argument, specify the endpoint required i.e. helloworld or 

+ task run_HTTPService helloworld

## API testing with postman

The API has been tested with Postman successfully. An example response from Postman is shown below.

For the endpoint /versionz:
<p align="center">
  <img src="Images/Postman_endpoint_versionz.png">
</p>

## Docker file

Run the following commands in the terminal to create the docker image and container.

+ docker build -t python-httpservice .
+ docker run python-httpservice



