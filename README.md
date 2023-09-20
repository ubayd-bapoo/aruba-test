# Setting Up and Running an Application with Docker and Python
This README file provides step-by-step instructions on how to set up and run a Python 
application using both Docker and a normal Python environment. This guide assumes you 
have Docker installed on your system and a basic understanding of Python.

## Table of Contents
- [Clone the Repository](#1-clone-the-repository)
- [Setting Up the Python Application](#2-setting-up-the-python-application)
- [Running the Python Application Locally](#)
- [Dockerize the Application](#section-1)
- [Building the Docker Image](#section-1)
- [Running the Dockerized Application](#section-1)

### 1. Clone the Repository
Clone the repository containing your Python application to your local machine using Git 
or by downloading the ZIP file from your source code hosting platform (e.g., GitHub).

### 2. Setting Up the Python Application
Before we proceed with Dockerization, make sure your Python application works correctly 
in a normal Python environment. This typically involves creating a virtual environment, 
installing dependencies, and testing the application.
<pre>
```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'

# Install application dependencies
pip install -r requirements.txt

# Test the application
python service.py
```
</pre>




docker build -t aruba-test .

uvicorn service:app --host 0.0.0.0 --port 8000 --reload