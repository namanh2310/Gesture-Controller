import cv2
import mediapipe as mp
# import pandas as pd  
import os
import numpy as np 
import time
import pickle
from get_score import image_processed
import cv2 as cv

with open('model_5.pkl', 'rb') as f:
    svm = pickle.load(f)

start_time = time.time()
prev_prediction = None
same_prediction_duration = 0
threshold_duration = 1.5

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
i = 0    
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    data = image_processed(frame)
    
    data = np.array(data)
    y_pred = svm.predict(data.reshape(-1,63))
    
    if y_pred != prev_prediction:
        prev_prediction = y_pred
        start_time = time.time()
        same_prediction_duration = 0
    else:
        same_prediction_duration = time.time() - start_time

    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50, 100)
    fontScale = 3
    color = (255, 0, 0)
    thickness = 5
    frame = cv2.putText(frame, str(y_pred[0]), org, font, 
                    fontScale, color, thickness, cv2.LINE_AA)
    cv.imshow('frame', frame)

    if same_prediction_duration >= threshold_duration:
        print(str(y_pred[0]))

    if str(y_pred[0]) == 'close 2':
        cv.imwrite('test.png',frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
