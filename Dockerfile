# Pull base image
FROM python:3.9-slim


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Note: these were here before we added docker, but we want to use our own requirements through poetry instead of pipenv
# COPY Pipfile Pipfile.lock /code/
# RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /code/
