import cv2
import mediapipe as mp
import urllib.request
import os

model_path = 'hand_landmarker.task'
if not os.path.exists(model_path):
    print("📥 Скачиваю модель MediaPipe...")
    url = 'https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task'
    urllib.request.urlretrieve(url, model_path)
    print("✅ Модель загружена!")

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.VIDEO,
    num_hands=2,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5
)


detector = HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)
print("Покажи руки в кадр!")

frame_timestamp_ms = 0

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    detection_result = detector.detect_for_video(mp_image, frame_timestamp_ms)
    frame_timestamp_ms += 33


    if detection_result.hand_landmarks:
        for hand_landmarks in detection_result.hand_landmarks:
            h, w, _ = frame.shape
            

            for landmark in hand_landmarks:
                x, y = int(landmark.x * w), int(landmark.y * h)
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
            
            connections = [
                (0, 1), (1, 2), (2, 3), (3, 4),
                (0, 5), (5, 6), (6, 7), (7, 8),
                (0, 9), (9, 10), (10, 11), (11, 12),
                (0, 13), (13, 14), (14, 15), (15, 16),
                (0, 17), (17, 18), (18, 19), (19, 20),
                (5, 9), (9, 13), (13, 17)
            ]
            
            for connection in connections:
                start = hand_landmarks[connection[0]]
                end = hand_landmarks[connection[1]]
                cv2.line(frame, 
                        (int(start.x * w), int(start.y * h)),
                        (int(end.x * w), int(end.y * h)),
                        (255, 0, 0), 2)

    cv2.imshow('Hand Tracking', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
detector.close()
cv2.destroyAllWindows()