# base image
FROM python:3.8

# set workdir
WORKDIR /app

# copy requirements to the container
COPY requirements.txt .

RUN pip install -r requirements.txt

# copy file with server script to the container
COPY server.py .

# define port
EXPOSE 8080

# run commands
CMD ["python", "server.py"]