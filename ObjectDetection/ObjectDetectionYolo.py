import cv2
import os
import urllib.request

# URLs
YOLO_CFG_URL = "https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4.cfg"
YOLO_WEIGHTS_URL = "https://github.com/AlexeyAB/darknet/releases/download/yolov4/yolov4.weights"
COCO_NAMES_URL = "https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names"

# File paths
YOLO_CFG = "yolov4.cfg"
YOLO_WEIGHTS = "yolov4.weights"
COCO_NAMES = "coco.names"

print("Download start...")
# Download files if missing
def download_file(url, filename):
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)

download_file(YOLO_CFG_URL, YOLO_CFG)
download_file(YOLO_WEIGHTS_URL, YOLO_WEIGHTS)
download_file(COCO_NAMES_URL, COCO_NAMES)

print("Download complete...")

# Load class labels
with open(COCO_NAMES, 'r') as f:
    labels = [line.strip() for line in f.readlines()]

# Load YOLO network
net = cv2.dnn.readNet(YOLO_WEIGHTS, YOLO_CFG)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

# Get output layer names
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Colors for each class
colors = [(0, 255, 0) for _ in range(len(labels))]

# Open webcam
cap = cv2.VideoCapture(0)
print("starting Capture...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width = frame.shape[:2]

    # Create blob from image
    blob = cv2.dnn.blobFromImage(frame, scalefactor=1/255.0, size=(416, 416), swapRB=True, crop=False)
    net.setInput(blob)

    # Forward pass
    outputs = net.forward(output_layers)

    boxes = []
    confidences = []
    class_ids = []

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = int(scores.argmax())
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x, center_y, w, h = (detection[0:4] * [width, height, width, height]).astype("int")
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, int(w), int(h)])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Non-max suppression
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=0.5, nms_threshold=0.4)

    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = f"{labels[class_ids[i]]}: {confidences[i]*100:.1f}%"
            cv2.rectangle(frame, (x, y), (x + w, y + h), colors[class_ids[i]], 2)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, colors[class_ids[i]], 2)

    cv2.imshow("YOLOv4 Object Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
