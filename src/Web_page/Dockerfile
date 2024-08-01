# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /Web_page

# Copy the current directory contents into the container at /Web_page
COPY . /Web_page

# Install dependencies
RUN apt-get update && \
    apt-get install -y gcc python3-spidev && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install spidev

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME Web_page

# Run app.py when the container launches
CMD ["python", "main.py"]
