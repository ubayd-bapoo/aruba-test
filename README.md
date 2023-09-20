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