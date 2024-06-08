import cv2
import mediapipe as mp


# data_set_theme = [words]

# for word in words:
#     if image detection == __doc__
    #  display green screen
    

cap = cv2.VideoCapture(0) # 0 uses web camera, 1 accesses phone 

# Create a gesture recognizer object
base_options = python.BaseOptions(model_asset_path = "gesture_recognizer.task")
options = vision.GestureRecognizerOptions(
    base_options = base_options,
    running_mode = vision.RunningMode.LIVE_STREAM,
    result_callback = hand_recognition_results
)
recognizer = vision.GestureRecognizer.create_from_options(options)

while True:
    success, frame = cap.read()
    # Exit loop if the frame reading isn't successful
    if not success:
        break 

    # Convert each frame to rgb images so mediapipe's model can detect it
    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(
    image_format = mp.ImageFormat.SRGB,
    data = rgb_image
    )

    recognizer.recognize_async(mp_image, frame)

    # Display frame
    cv2.imshow("Frame Image", frame)
    
    # Pauses/Waits 1 millisecond before viewing the next frame
    # if cv2.waitKey(1) & OxFF == ord('q'):
    #     break #exits if key pressed
    
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows


# go back and add the minimum hand detection as 1 


words = []

# for word in words:
#     if image detection == __doc__
    #  display green screen



