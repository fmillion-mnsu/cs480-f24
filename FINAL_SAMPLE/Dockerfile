# This Dockerfile shows you how you might create a container for Python-based microservices.

# YOU CANNOT USE THIS FILE AS-IS. YOU NEED TO MAKE CHANGES TO MAKE IT MATCH YOUR PROJECT.

# Use the official Python image from the Docker Hub 
FROM python:3.11 AS base

# Copy requirements.txt into the application directory
COPY requirements.txt /app/requirements.txt

# Set the working directory to /app
WORKDIR /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# **  Assume your first microservice is login.py  **

FROM base AS login_service

CMD ["python", "login.py"]

# Flask listens on port 5000.
EXPOSE 5000

# **  Assume your second microservice is user.py  **

FROM base AS user_service

CMD ["python", "login.py"]

EXPOSE 5000

# **  Repeat the above for as many microservices as you have.  **
