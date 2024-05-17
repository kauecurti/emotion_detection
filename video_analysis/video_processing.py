# video_analysis/video_processing.py
import cv2
from deepface import DeepFace


def analyze_video(video_path, face_cascade, task, total_frames):
    emotions = []

    cap = cv2.VideoCapture(video_path)
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            roi_color = frame[y:y + h, x:x + w]
            try:
                result = DeepFace.analyze(roi_color, actions=['emotion'], enforce_detection=False)
                if isinstance(result, list):
                    result = result[0]
                dominant_emotion = result['dominant_emotion']
                emotion_score = result['emotion'][dominant_emotion]
                emotions.append((frame_count / frame_rate, dominant_emotion, emotion_score))
            except Exception as e:
                print(f"Error analyzing frame {frame_count}: {e}")

        frame_count += 1
        task.update_state(state='PROGRESS', meta={'current': frame_count, 'total': total_frames})

    cap.release()
    return emotions
