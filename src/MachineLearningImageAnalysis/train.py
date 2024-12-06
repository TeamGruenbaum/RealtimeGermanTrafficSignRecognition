import ultralytics

model = ultralytics.YOLO('yolov8x.pt')
model.train(data='/Mixed.yolov8/data.yaml', epochs=50)
