# With inspiration from https://colab.research.google.com/drive/1OiyJNXnIow-tXfj_ZhnjMNOFC96d8iEe
# and https://courses.opencv.org/courses/course-v1:OpenCV+Bootcamp+CV0/courseware/457799bde2064b749df7fb0c0a741b5f/59fc30bb940d4549a51ead841a0f7d04/1
# By Gunnar Storebo


import cv2
import os

# Paths to model and config
modelFile  = os.path.join("models", "ssd_mobilenet_v2_coco_2018_03_29", "frozen_inference_graph.pb")
configFile = os.path.join("models", "ssd_mobilenet_v2_coco_2018_03_29.pbtxt")

# Load the model
net = cv2.dnn_DetectionModel(modelFile, configFile)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# Load COCO class labels (optional for better labeling)
classNames = []
with open("models/coco.names", "r") as f:  # Make sure you have this file
    classNames = f.read().rstrip('\n').split('\n')

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    classIds, confs, bbox = net.detect(frame, confThreshold=0.5)

    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            label = f"{classNames[classId - 1]}: {round(confidence * 100, 2)}%" if classId <= len(classNames) else str(classId)
            cv2.rectangle(frame, box, color=(0, 255, 0), thickness=2)
            cv2.putText(frame, label, (box[0], box[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
