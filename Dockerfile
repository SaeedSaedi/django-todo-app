FROM python:3.12.3-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y

# Copy application code
COPY . /app

# Install Python dependencies
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# Set environment variable
ENV PYTHONUNBUFFERED=1

