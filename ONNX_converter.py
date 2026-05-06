from ultralytics import YOLO
import os

#directory = r'PATH\TO\YOUR\.PT\FILE'
os.chdir(directory)
model = YOLO("best.pt")
model.export(format="onnx")
