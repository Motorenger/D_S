FROM python:3.9.13-alpine3.15

# setting working directory
WORKDIR usr/src/app

# setting env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# installing dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# copping project
COPY . .
