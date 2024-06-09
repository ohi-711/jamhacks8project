from flask import Flask, render_template, Response, jsonify, request
import cv2
import mediapipe as mp
import json
import subprocess

app = Flask(__name__)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

def generate_frames():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Process the frame with MediaPipe
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame_rgb)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/instructions')
def instructions():
    return render_template('instructions.html')

@app.route('/camera')
def camera():
    return render_template('main.html')

@app.route('/scores')
def scores():
    return render_template('scores.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_scores')
def get_scores():
    with open('scores.json') as json_file:
        data = json.load(json_file)
    return jsonify(data)

@app.route('/run_script', methods=['POST'])
def run_script():
    try:
        # Run the Python script
        result = subprocess.run(['python', 'gesturedetector.py'], capture_output=True, text=True)
        output = result.stdout
        return jsonify({'output': output})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)