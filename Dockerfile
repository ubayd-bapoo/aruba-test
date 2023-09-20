FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the rest of your application code into the container
COPY . /app/

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt && apt-get update; apt-get install curl -y

# Expose the port that the FastAPI application will run on (default is 8000)
EXPOSE 8000

HEALTHCHECK --interval=60s --timeout=5s \
    CMD curl -s --fail http://localhost:8000/meta/health

# Command to run your FastAPI application using python
ENTRYPOINT ["python", "service.py"]