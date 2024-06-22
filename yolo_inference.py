from ultralytics import YOLO

model = YOLO("yolov8x.pt")

model.predict("./input_videos/image.png", save=True)

