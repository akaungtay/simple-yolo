from fastapi import FastAPI, File, UploadFile
# from typing import List
from PIL import Image
import io
from ultralytics import YOLO

# Initialize FastAPI app
app = FastAPI()

# Load YOLO11 model
model = YOLO('yolo11n.pt')

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Read image file
    image_bytes = await file.read()
    img = Image.open(io.BytesIO(image_bytes))
    
    # Perform inference
    results = model(img)
    res = []
    for result in results:
        if result:
            for id,conf in zip(result.boxes.cls,result.boxes.conf):
                res += [{result.names[int(id)]: round(float(conf),2)}]  
    return res
