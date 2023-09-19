FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . /app/

# Expose the port that the FastAPI application will run on (default is 8000)
EXPOSE 8000

# Command to run your FastAPI application using Uvicorn
CMD ["uvicorn", "service:app", "--host", "0.0.0.0", "--port", "8000"]