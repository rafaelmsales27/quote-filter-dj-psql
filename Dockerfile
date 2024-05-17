FROM python:3.11-slim-buster


# Setting wotk dir
WORKDIR /usr/src/app

# Env variables
# Prevents Python from writing pyc files to disc
ENV PYTHONUNBUFFERED 1 
# Prevents Python from buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE 1

# Install psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
# Flake 8 helps maintin pep8 compliance
RUN pip install --upgrade pip pipenv flake8
COPY Pipfile* ./
RUN pipenv install --system --ignore-pipfile

# Copy our code to the docker container
COPY . .



# Run flake8 to check linter suggestions
RUN flake8 --ignore=E501,F401 .

