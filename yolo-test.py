from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")



# Perform object detection on an image
results = model("./bus.jpg")
print("--result--")
res = []
for result in results:
    if result:
        for id,conf in zip(result.boxes.cls,result.boxes.conf):
            res += [{result.names[int(id)]: round(float(conf),2)}]
        # print(result.names[int(id)],'-',float(conf))
print(res)
