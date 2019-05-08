# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.7

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# create root directory for our project in the container
RUN mkdir /src
RUN apt-get -y update
RUN apt-get -y install binutils libproj-dev gdal-bin

# Set the working directory to /src
WORKDIR /src

# Copy the current directory contents into the container at /src
ADD . /src/

# Install any needed packages specified in requirements.txt
RUN pip install -r src/requirements/requirements.txt
