import cv2
import mediapipe as mp

# data_set_theme = [words]

# for word in words:
#     if image detection == __doc__
    #  display green screen
    
cap = cv2.VideoCapture(0) # 0 uses web camera, 1 accesses phone 

while True:
    success, frame = cap.read()
    # Exit loop if the frame reading isn't successful
    if not success:
        break 
    # Display frame
    cv2.imshow("Frame Image", frame)
    # Pauses/Waits 1 millisecond before viewing the next frame
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows