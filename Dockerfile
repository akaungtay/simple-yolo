# Base Image
FROM ubuntu/python:3.10-22.04

# creating working folder
WORKDIR /app

# copy code
COPY . .

# Update pip
RUN pip install --upgrade pip

# Install additional dependencies for KServe and FastAPI
RUN pip install -r requirements.txt

# Set the command to run the FastAPI server
CMD ["uvicorn", "yolo_kserve:app", "--host", "0.0.0.0", "--port", "8000"]
