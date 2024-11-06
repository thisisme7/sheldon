# Use an official Python runtime as a base image
FROM python:3.10.7-alpine

# Set the working directory inside the container
WORKDIR /app
RUN pip install --no-cache-dir --upgrade pip

COPY requirements.txt /app/

# Install the required dependencies (if you have any)
RUN pip3 install -r requirements.txt

# Copy the application code to the container
COPY . /app/

# Expose the port on which your Flask app runs 
EXPOSE 8002

# Command to run your Flask application
CMD ["gunicorn", "--bind", "172.17.0.2:8002", "gui:app"]
