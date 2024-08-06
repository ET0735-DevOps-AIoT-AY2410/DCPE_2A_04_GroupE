# Use the official Python image for ARM architecture
FROM arm32v7/python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhost.org -r requirements.txt

# Copy the application code into the container
COPY ./Web_page /app/Web_page
COPY ./hal /app/hal
COPY ./SPI-Py /app/SPI-Py

# Set environment variable for SPI path
ENV SPI_PATH /app/SPI-Py

# Install SPI driver
WORKDIR $SPI_PATH
RUN python3 setup.py install

# Install additional Python packages
RUN pip install --no-cache-dir rpi.gpio smbus spidev

# Set the working directory to where the application code is
WORKDIR /app/Web_page

# Expose port 5000 for the web application
EXPOSE 5000

# Run the Flask application
CMD ["python", "main.py"]
