import cv2
import numpy as np
cap=cv2.VideoCapture(0)
back=cv2.imread('./image.jpg')

while cap.isOpened():
    ret,frame=cap.read()
    if ret:
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        blue = np.uint8([[[255,0,0]]])
        hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
        
        l_blue = np.array([100, 100, 0])    #lower range
        u_blue = np.array([255, 255, 255])  #upper range
        
        mask = cv2.inRange(hsv, l_blue, u_blue)
        part1 = cv2.bitwise_and(back, back, mask=mask)  #to show background
        
        mask = cv2.bitwise_not(mask)
        part2 = cv2.bitwise_and(frame, frame, mask=mask)  #to show frame
        
        cv2.imshow("cloak", part1 + part2)
        if cv2.waitKey(5)==ord('q'):
            break
cap.release()
