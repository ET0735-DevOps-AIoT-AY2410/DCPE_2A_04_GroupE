# Use the official Python image from the Docker Hub
FROM arm32v&/python:3
#FROM python:3.9-alpine

# Set the working directory
ENV SPI_PATH /app/website/SPI-Py
WORKDIR /app

# Copy the current directory contents into the container at /Web_page
COPY . .

# Install dependencies
# Install SPI driver
WORKDIR $SPI_PATH
RUN python3 setup.py install
#RUN apt-get install raspi-config
#RUN raspi-config
RUN pip install rpi.gpio

WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "main.py"]

