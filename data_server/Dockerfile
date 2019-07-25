# base image
FROM python:3

# set working directory
WORKDIR /app

# install and catch app dependencies
COPY . /app
RUN pip install --upgrade pip
RUN pip install pandas
RUN pip install Flask
RUN pip install Flask-Cors

# start app
CMD [ "python", "pythontest.py" ]

# Docker Build and  Run
# docker build -t pythontest .
# docker run -it -v ${PWD}:/app -p 5000:5000 --rm pythontest [Remove -it to run via container]