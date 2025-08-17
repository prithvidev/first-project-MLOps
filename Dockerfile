#using python 3.10 version as base image
from python:3.10

#Setting working directory inside container
WORKDIR /app

#Copying all the files inside the container including model file, etc.
COPY . /app

#Installing requirements inside a container
RUN pip install -r requirements.txt

#Command to run FASRAPI application through uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
