# API Testing with Docker: Project Report

## Introduction
Docker containers are a popular technology for simplifying application development, packaging, and deployment processes. This project focuses on creating Docker containers to test an API for sentiment analysis. The goal is to validate the functionality of the API endpoints before deployment.

## Exercise Overview
For this exercise, I created of Docker containers to test an API for sentiment analysis. The API allows users to predict whether a sentence is positive or negative. The entry points of the API include `/status`, `/permissions`, `/v1/sentiment`, and `/v2/sentiment`. We aimed to create tests to validate the functionality of these entry points using Docker containers.

## Given

A team has created an application that allows to use a sentiment analysis algorithm: it allows to predict if a sentence is positive or negative. This API will be deployed in a container whose image is for the moment datascientest/fastapi:1.0.0.

Let's look at the entry points of our API:

/status returns 1 if the API is running
/permissions returns a user's permissions
/v1/sentiment returns the sentiment analysis using an old model
/v2/sentiment returns the sentiment analysis using a new template
The /status entry point simply checks that the API is working. The /permissions entry point allows someone, identified by a username and a password to see which version of the template they have access to. Finally the last two take a sentence as input, check that the user is identified, check that the user has the right to use this template and if so, return the sentiment score: -1 is negative; +1 is positive.
To download the image, run the following command

docker image pull datascientest/fastapi:1.0.0

docker container run -p 8000:8000 datascientest/fastapi:1.0.0.

The API is available on port 8000 of the host machine. At the entry point /docs you can find a detailed description of the entry points

## Tests
### Authentication
In this first test, we are going to check that the identification logic works well. To do this, we will need to make GET requests on the `/permissions` entry point. We know that two users exist: alice and bob, and their passwords are wonderland and builder. We'll try a third test with a password that doesn't work: clementine and mandarine. The first two requests should return a 200 error code while the third should return a 403 error code.

### Authorization
In this second test, we will verify that our user authorization logic is working properly. We know that bob only has access to v1 while alice has access to both versions. For each of the users, we will make a query on the `/v1/sentiment` and `/v2/sentiment` entry points: we must then provide the arguments username, password, and sentence which contains the sentence to be analyzed.

### Content
In this last test, we check that the API works as it should. We will test the following sentences with the alice account:
- "life is beautiful"
- "that sucks"
For each version of the model, we should get a positive score for the first sentence and a negative score for the second sentence. The test will consist of checking the positivity or negativity of the score.

## Building the Tests
- Each test is encapsulated in a separate Docker container to maintain modularity and flexibility.
- Docker images are created for each test scenario, allowing easy deployment and execution.

## Deliverables
To fulfill the exercise requirements, the following files and components were prepared:
- **Dockerfile**: Python files used in Docker images.
- **docker-compose.yml**: Sequence of tests to be performed organized in a Docker Compose file.
- **setup.sh**: Contains commands for building images and launching Docker Compose.
- **log.txt**: Result of the test logs generated during the execution of the pipeline.

## Conclusion
This project demonstrates the use of Docker containers for testing an API before deployment. By encapsulating each test scenario in a Docker container, we ensure modularity and flexibility in the testing process.
