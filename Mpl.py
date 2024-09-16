import cv2
import mediapipe as mp
import numpy as np
from exercise_data import EXERCISES
import pyttsx3

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Initialize text-to-speech engine
engine = pyttsx3.init()

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    if angle > 180.0:
        angle = 360 - angle
    return angle

def get_coordinates(landmarks, keypoint):
    return [landmarks[mp_pose.PoseLandmark[keypoint.upper()].value].x,
            landmarks[mp_pose.PoseLandmark[keypoint.upper()].value].y]

def detect_phase(angles, exercise_data):
    for phase, conditions in exercise_data["phases"].items():
        if all(conditions[angle_name]["min"] <= angles[angle_name] <= conditions[angle_name]["max"] 
               for angle_name in conditions):
            return phase
    return "transition"

def detect_mistakes(angles, exercise_data, phase):
    mistakes = []
    for mistake in exercise_data["mistakes"]:
        if mistake["condition"](angles, phase):
            mistakes.append(mistake["message"])
    return mistakes

def count_reps(exercise_name):
    cap = cv2.VideoCapture(0)
    counter = 0
    current_phase = None
    prev_phase = None
    rep_progress = []
    
    exercise_data = EXERCISES[exercise_name]
    rep_states = list(exercise_data["rep_conditions"].values())
    
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.pose_landmarks:
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                landmarks = results.pose_landmarks.landmark
                
                # Calculate relevant angles
                angles = {}
                for angle_name, *points in exercise_data["angles"]:
                    coords = [get_coordinates(landmarks, point) for point in points]
                    angles[angle_name] = calculate_angle(*coords)

                current_phase = detect_phase(angles, exercise_data)
                
                # Count reps
                if current_phase != prev_phase:
                    if current_phase in rep_states:
                        if not rep_progress or current_phase != rep_progress[-1]:
                            rep_progress.append(current_phase)
                    
                    if rep_progress == rep_states:
                        counter += 1
                        rep_progress = []
                        print(f"Rep {counter} completed!")

                # Detect mistakes
                mistakes = detect_mistakes(angles, exercise_data, current_phase)
                for i, mistake in enumerate(mistakes):
                    cv2.putText(image, mistake, (10, 90 + i*30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    engine.say(mistake)
                    engine.runAndWait()

                prev_phase = current_phase

            cv2.putText(image, f'Reps: {counter}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(image, f'Phase: {current_phase}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            cv2.imshow('Pose Estimation', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    exercise_name = input("Enter exercise name (squats/pushups): ").lower()
    if exercise_name in EXERCISES:
        count_reps(exercise_name)
    else:
        print("Invalid exercise name. Please choose 'squats' or 'pushups'.")