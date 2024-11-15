# Base Image
FROM python:3.10-slim

# Install libglib2.0 which includes libgthread
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

# creating working folder
WORKDIR /app

# copy code
COPY . .

# Update pip
RUN pip install --upgrade pip

# Install additional dependencies for KServe and FastAPI
RUN pip install -r requirements.txt

# Set the command to run the FastAPI server
CMD ["uvicorn", "yolo-kserve:app", "--host", "0.0.0.0", "--port", "8000"]
