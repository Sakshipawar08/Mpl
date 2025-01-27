import cv2
import mediapipe as mp
import numpy as np

#Initialize pose
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

#video feed
cap = cv2.VideoCapture(0)
##setup media instance
with mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()

        #Recolor image to RGB
        image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        #Make detection
        results = pose.process(image)

        #Recolor image to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR) 

        #Render detections
        mp_drawing.draw_landmarks(image,results.pose_landmarks,mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(0,0,6), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(245,0,0), thickness=2, circle_radius=2)
                                  ) 

        cv2.imshow('mediapipe feed',image)

        if cv2.waitKey(10) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

mp_drawing.DrawingSpec

cap = cv2.VideoCapture(0)
##setup media instance
with mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()

        #Recolor image to RGB
        image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        #Make detection
        results = pose.process(image)

        #Recolor image to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

        #extract landmark
        try:
            landmarks = results.pose_landmarks.landmark
            print(landmarks)
        except:
            pass 

        #Render detections
        mp_drawing.draw_landmarks(image,results.pose_landmarks,mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(0,0,6), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(245,0,0), thickness=2, circle_radius=2)
                                  ) 

        cv2.imshow('mediapipe feed',image)

        if cv2.waitKey(10) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

mp_drawing.DrawingSpec

len(landmarks)
for lndmark in mp_pose.PoseLandmark:
    print(lndmark)

landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].visibility
landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value]
landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]

def calculate_angle(a,b,c):
    a = np.array(a) #first
    b = np.array(b) #middle
    c = np.array(c) #last
    radians = np.arctan2(c[1]-b[1] ,c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    if angle >180.0:
        angle = 360-angle
    return angle

shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
shoulder,elbow,wrist
calculate_angle(shoulder,elbow,wrist)

tuple(np.multiply(elbow,[640,480]).astype(int))

cap = cv2.VideoCapture(0)
##setup media instance
with mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()

        #Recolor image to RGB
        image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        #Make detection
        results = pose.process(image)

        #Recolor image to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

        #extract landmark
        try:
            landmarks = results.pose_landmarks.landmark
            #get co-ordinates
            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            #calculate angle
            angle = calculate_angle(shoulder,elbow,wrist)
            # visualize
            cv2.putText(image,str(angle),
                        tuple(np.multiply(elbow, [640,480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255), 2,cv2.Line_AA)
            
        except:
            pass 

        #Render detections
        mp_drawing.draw_landmarks(image,results.pose_landmarks,mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(0,0,6), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(245,0,0), thickness=2, circle_radius=2)
                                  ) 

        cv2.imshow('mediapipe feed',image)

        if cv2.waitKey(10) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
#curl counter variable
counter = 0
stage = None
##setup media instance
with mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()

        #Recolor image to RGB
        image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        #Make detection
        results = pose.process(image)

        #Recolor image to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

        #extract landmark
        try:
            landmarks = results.pose_landmarks.landmark
            
            #get co-ordinates
            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            #calculate angle
            angle = calculate_angle(shoulder,elbow,wrist)
            # visualize angle
            cv2.putText(image,(str(angle)),
                        tuple(np.multiply(elbow, [640,480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255), 2,cv2.Line_AA)
            #curl counter logic
            if angle > 160:
                stage = "down"
            if angle < 30 and stage == 'down':
                stage = "up"
                counter += 1
                print(counter)           
        except:
            pass

        #render curl counter
        # setup status box
        cv2.rectangle(image, (0,0),(255,73),(245,117,16), -1)

        #rep data
        cv2.putText(image,'REPS',(15,12),
                    cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1,cv2.LINE_AA)
        cv2.putText(image, str(counter),
                    (10,60),
                    cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255), 2,cv2.Line_AA)
        
        #stage data
        cv2.putText(image,'STAGE',(65,12),
                    cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1,cv2.LINE_AA)
        cv2.putText(image, stage,
                    (60,60),
                    cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255), 2,cv2.Line_AA)
         
        #Render detections
        mp_drawing.draw_landmarks(image,results.pose_landmarks,mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(0,0,6), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(245,0,0), thickness=2, circle_radius=2)
                                  ) 

        cv2.imshow('mediapipe feed',image)

        if cv2.waitKey(10) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
