# Setting Up and Running an Application with Docker and Python
This README file provides step-by-step instructions on how to set up and run the Python 
application using both Docker and a normal Python environment for the Aruba test. This 
guide assumes you have Docker installed on your system and a basic understanding of Python.

## Table of Contents
- [Clone the Repository](#1-clone-the-repository)
- [Setting Up the Python Application](#2-setting-up-the-python-application)
- [Running the Python Application Locally](#3-running-the-python-application-locally)
- [Building the Docker Image](#4-building-the-docker-image)
- [Running the Dockerized Application](#5-running-the-dockerized-application)
- [Environment Variables](#6-environment-variables)
- [Unit Test](#7-unit-test)
- [API Documentation](#8-api-documentation)

### 1. Clone the Repository
Clone the repository containing the Python application to your local machine using Git 
or by downloading the ZIP file from the source code on GitHub.
```bash
git clone git@github.com:ubayd-bapoo/aruba-test.git
cd aruba_test
```

### 2. Setting Up the Python Application
Lets make sure the Python application works correctly in a normal Python environment. 
This typically involves creating a virtual environment, installing dependencies, and 
testing the application.

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'

# Install application dependencies
pip install -r requirements.txt

# Test the application
python service.py  # In the service_app folder
```

### 3. Running the Python Application Locally
To run the application in your local Python environment, you can use the following command:
```bash
python service.py  # In the service_app folder
```

### 4. Building the Docker Image
The Dockerfile sets up a basic Python environment and copies the application files into 
the container. It also installs all necessary dependencies from requirements.txt and 
specifies the command to run when the container starts.
To build a Docker image of the Python application, navigate to the project directory 
(where the Dockerfile is located) and run the following command:
```
docker build -t aruba-test .
```

### 5. Running the Dockerized Application
Once the Docker image is built successfully, you can run the Python application within 
a Docker container:
```bash
docker run -p 8000:8000 aruba-test
```

### 6. Environment Variables
To run this application, you'll need to set up some environment variables. These variables
 are used to configure various aspects of the application. Here's a list of the required 
 environment variables and their descriptions:
 1. **KEY**: To access external APIs, you'll need to obtain an API key and set it as 
 the `KEY` environment variable.

### 7. Unit Test
To run the unit tests for this application, follow these steps:
```bash
   pytest unit_tests.py
```
#### Automated Testing with GitHub Actions

I have set up a GitHub Actions workflow that automatically runs pytest for our unit tests
 whenever changes are pushed to the repository's `main` branch. This ensures that our code
  is continuously tested for correctness.

The workflow configuration can be found in the [`.github/workflows/python-app.yml`](.github/workflows/python-app.yml) file. Here's how it works:

- Whenever you push changes to the `main` branch, GitHub Actions will automatically 
trigger the workflow.
- The workflow will use the `pytest` command to execute the tests defined in the 
`unit_tests.py` file.
- The results of the tests will be displayed in the GitHub Actions logs.

You can always check the status of the tests by visiting the "Actions" tab in this 
repository. If there are any issues with the tests, you will be notified.

By leveraging GitHub Actions, we ensure that our codebase remains reliable and that new
 contributions are thoroughly tested before being merged into the main branch.

### 8. API Documentation
The API documentation is powered by FastAPI's built-in Swagger integration. This interactive documentation makes it 
easy to explore and understand the API endpoints.
- **Access API Documentation**: To explore our API documentation and test the endpoints 
interactively, simply visit [Swagger UI](http://localhost:8000/docs) (http://localhost:8000/docs) when the application
 is running locally.

- **Automatic Documentation**: We've designed our API using FastAPI, which automatically
 generates documentation based on the code, including request and response models and 
 descriptions.

FastAPI's Swagger UI provides a user-friendly way to understand and use our API. You can
 interact with the available endpoints, view request and response models, and even make
  test requests right from the documentation.

Feel free to dive into the documentation to get a better understanding of how to use our
 API effectively.

![FastAPI Swagger UI](https://fastapi.tiangolo.com/img/tutorial/tutorial-02-swagger-ui.png)

Note: In a production environment, replace `http://localhost:8000/docs` with the actual
 URL where your API is hosted.