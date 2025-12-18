import cv2 as cv
import os
import time

#Use the videocam
capture = cv.VideoCapture(0)

#Capture the reference frame to compare with
isTrue, prev_frame = capture.read()
prev_gray = cv.cvtColor(prev_frame, cv.COLOR_BGR2GRAY)
prev_gray = cv.GaussianBlur(prev_gray, (5,5), cv.BORDER_DEFAULT)

#Snapshot values initialization
snapshot_dir = "motion_snapshots"
last_snapshot_time = 0
snapshot_interval = 2


#Capture the moving frames
while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break


    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

    diff = cv.absdiff(prev_gray, blur) #compares with current frame and reference frame  

    _, thresh = cv.threshold(diff, 25, 255, cv.THRESH_BINARY) # gives yes or no for motion detected
    dilated = cv.dilate(thresh, None, iterations=2)  #to dilate threshold and remove unecessary whites and remove those greys

    contours, _ = cv.findContours(dilated,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) # to make a shape or point of the moved regions

    motion_detected = False

    for contour in contours:                          #to check if those points are unwanted or not , ex-noise
        if cv.contourArea(contour) < 500:
          continue

        motion_detected = True

        x, y, w, h = cv.boundingRect(contour) # to make the rectangle boxes on the movement
        cv.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
    
    current_time = time.time()
    if motion_detected and (current_time - last_snapshot_time > snapshot_interval):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"{snapshot_dir}/motion_{timestamp}.jpg"

        cv.imwrite(filename, frame)
        print("Snapshot saved:", filename)

        last_snapshot_time = current_time

    cv.imshow('Webcam', frame)
    # cv.imshow('Gray', gray)
    # cv.imshow('Blur', blur)
    # cv.imshow("Difference", diff) #If any difference or movement white region , rest black
    # cv.imshow("Threshold", thresh) #Full black screen, if movement then region becomes white
    # cv.imshow("Dilated", dilated)


    prev_gray = blur #so that the full screen doesnt turn white after a lot of movement



    if cv.waitKey(1) & 0xFF == ord('q'):
        break




capture.release()
cv.destroyAllWindows()
