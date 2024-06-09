import cv2
import mediapipe as mp
import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as mp_draw
import mediapipe.python.solutions.drawing_styles as drawing_styles
import time

from wordbank import words
from wordbank import expected_word_landmarks

# Define the hand-landmarks for each word in the game's dataset (dictionary)
# We are using static ASL words 
word_index = 0

def evaluate_gesture(word, detected_landmarks):
    correct_landmarks = expected_word_landmarks[word]
    for i, landmark in enumerate(detected_landmarks):
        if i >= len(correct_landmarks):
            break 
        
        if abs(landmark.x - correct_landmarks[i][0]) > 0.25 or \
           abs(landmark.y - correct_landmarks[i][1]) > 0.25 or \
           abs(landmark.z - correct_landmarks[i][2]) > 0.25 :
            return False
    return True 

# Create a hands object
hands = mp_hands.Hands(
    static_image_mode = False, # video, not images
    max_num_hands = 2,
    min_detection_confidence = 0.7 # continue if atleast 70% of hands are detected

)

# Initialize camera
CAM_WIDTH = 640
CAM_HEIGHT = 480
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, CAM_WIDTH)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, CAM_HEIGHT)

while cam.isOpened():
    success, frame = cam.read()
    if not success:
        print("Camera Failed")
        continue

    if cv2.waitKey(20) & 0xff == ord('q'):
        break

    # Convert video frames to RGB so mediapipe can process them
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hands_detected = hands.process(frame)

    # draws the landmarks on the screen
    if hands_detected.multi_hand_landmarks:
        for hand_landmarks in hands_detected.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frame, 
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                drawing_styles.get_default_hand_landmarks_style(),
                drawing_styles.get_default_hand_connections_style(),
            )
            if word_index >= len(words):
                 break
            elif evaluate_gesture(words[word_index], hand_landmarks.landmark):
                print(f"Correct, {words[word_index]}")
                # Only moves on to the next word if the word guessed was correct
                word_index += 1 
                time.sleep(2) # Delay between detecting next image
            else:
                print("Keep Trying!")

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.imshow("Display Screen", frame)
    
cam.release()
cv2.destroyAllWindows()

