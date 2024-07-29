# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /Web_page

# Copy the current directory contents into the container at /Web_page
COPY . /Web_page

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "main.py"]

