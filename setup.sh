#!/bin/bash

# Step 1: Build Docker images for Authentication, Authorization, Content tests
docker build -t authentication-test ./authentication_test
docker build -t authorization-test ./authorization_test
docker build -t content-test ./content_test

# Step 2: Run Docker Compose to orchestrate containers
docker-compose up -d

# Step 3: Wait for tests to complete
# You may need to adjust the sleep duration based on your test execution time
docker-compose down

