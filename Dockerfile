# Use an official Python runtime as a base image
FROM python:3.11-slim-bookworm

# Set the working directory inside the container
WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update -y
RUN chown -R daemon:daemon /app

USER daemon

ENV FLASK_ENV=production
# Expose the port on which your Flask app runs 
EXPOSE 8002

# Command to run your Flask application
CMD ["gunicorn", "--bind", "0.0.0.0:8002", "wsgi:app"]
