import time

import numpy as np
import cv2

cap = cv2.VideoCapture(-1)
time.sleep(30)
# Define the codec and create VideoWriter object
if (cap.isOpened() == False):
    print("Error opening video  file")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
start_time = time.time()

while (cap.isOpened()):
    ret, frame = cap.read()
    current_time = time.time()
    if ret == True:
        # frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame', frame)
    if (current_time - start_time) > 2:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()